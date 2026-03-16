import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    for _ in range(iterations):
        predictions = X @ theta                 # 2. Compute predictions h(x)
        errors = predictions - y                # 3. Compute error = h - y
        gradient = alpha * (X.T @ errors) / m   # 4. Compute gradient
        theta -= gradient                       # 5. Update weights for each iteration
    return np.round(theta.flatten(), 4)