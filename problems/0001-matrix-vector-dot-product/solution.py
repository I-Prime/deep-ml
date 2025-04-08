def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if not a or not a[0]:
        return -1

    num_cols = len(a[0])
    if len(b) != num_cols:
        return -1

    result = []
    for row in a:
        if len(row) != num_cols:
            return -1  # Ensure consistent row lengths
        dot = sum(row[i] * b[i] for i in range(num_cols))
        result.append(dot)

    return result
