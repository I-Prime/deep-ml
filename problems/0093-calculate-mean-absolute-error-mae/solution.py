import numpy as np

def mae(y_true, y_pred):
    """
    Calculate Mean Absolute Error between two arrays.

    Parameters:
        y_true (numpy.ndarray): Array of true values
        y_pred (numpy.ndarray): Array of predicted values

    Returns:
        float: Mean Absolute Error
    """
    # Your code here
    if y_true.size!=y_pred.size:
        raise ValueError("Both arrays must be  of the same size")
    if y_true.size==0:
        raise ValueError("Array cannot be Empty")
    return round(np.mean(np.abs(y_true-y_pred)),3)