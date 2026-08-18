from flask import Flask, render_template
from t57post import Post
import requests

app = Flask(__name__)

API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

def load_posts():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        posts_list = []
        for item in data:
            post_obj = Post(
                post_id=item["id"],
                title=item["title"],
                subtitle=item["subtitle"],
                body=item["body"]
            )
            posts_list.append(post_obj)
        return posts_list
        
    except Exception:
        return [
            Post(
                1, 
                "The Life of Cactus", 
                "Who knew that cacti lived such interesting lives.", 
                "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jicama salsify ."
            ),
            Post(
                2, 
                "Top 15 Things to do When You are Bored", 
                "Are you bored? Don't know what to do? Try these top 15 activities.", 
                "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere , decide to want nothing to do with my owner today."
            ),
            Post(
                3, 
                "Introduction to Intermittent Fasting", 
                "Learn about the newest health craze.", 
                "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
            )
        ]

post_objects = load_posts()

@app.route('/')
@app.route('/blog')
def get_all_posts():
    return render_template("t57index.html", all_posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = next((p for p in post_objects if p.id == index), None)
    return render_template("t57post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)