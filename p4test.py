import config

def test_regression_control_figures():
    """Verifies that baseline metrics match expected control figures within tolerance."""
    simulated_total_revenue = 154200.0  # Replace with actual output call or mock sum
    tolerance = 0.05
    
    variance = abs(simulated_total_revenue - config.CONTROL_TOTAL_REVENUE) / config.CONTROL_TOTAL_REVENUE
    assert variance <= tolerance, f"Regression failed: Revenue variance {variance:.2%}"