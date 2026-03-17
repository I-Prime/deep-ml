import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # 1. Convert to numpy arrays
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    
    # 2. Apply Normal Equation: (X^T * X)^-1 * X^T * y
    X_transpose = X.T
    theta = np.linalg.inv(X_transpose @ X) @ X_transpose @ y
    
    # 3. Round and preserve -0.0 sign using string formatting
    # Flatten the result and convert each element
    return [float(f"{val[0]:.4f}") for val in theta]