import uuid
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Product, Order, OrderStatus
from pydantic import BaseModel

router = APIRouter()

class CheckoutRequest(BaseModel):
    buyer_id: uuid.UUID
    product_id: uuid.UUID
    quantity: int
    idempotency_key: str

@router.post("/checkout")
async def checkout(req: CheckoutRequest, db: AsyncSession = Depends(get_db)):
    # 1. Idempotency Check: Return existing order if key was already used
    existing_order = await db.execute(
        select(Order).where(Order.idempotency_key == req.idempotency_key)
    )
    existing = existing_order.scalar_one_or_none()
    if existing:
        return {"status": "success", "order_id": existing.id, "replayed": True}

    # 2. Lock product row to safely update stock during concurrent checkouts
    prod_stmt = select(Product).where(Product.id == req.product_id).with_for_update()
    result = await db.execute(prod_stmt)
    product = result.scalar_one_or_none()

    if not product or product.stock < req.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock or invalid product")

    # 3. Reserve Stock & Create Order
    product.stock -= req.quantity
    total = float(product.price) * req.quantity
    
    new_order = Order(
        buyer_id=req.buyer_id,
        idempotency_key=req.idempotency_key,
        total_amount=total,
        status=OrderStatus.PENDING
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return {"status": "created", "order_id": new_order.id, "total": total}

@router.post("/payments/webhook")
async def payment_webhook(
    data: dict, 
    x_signature: str = Header(..., alias="X-Signature"),
    db: AsyncSession = Depends(get_db)
):
    # Process payment sandbox webhook
    order_id = data.get("order_id")
    event = data.get("event")

    order = await db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if event == "payment.succeeded" and order.status != OrderStatus.PAID:
        order.status = OrderStatus.PAID
        await db.commit()

    return {"status": "ok"}