def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    a,b,c,d=matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1]
    det_matrix=a*d- b*c
    if det_matrix==0:
        return None
    inverse=[[d/det_matrix,-b/det_matrix],[-c/det_matrix,a/det_matrix]]
    return inverse