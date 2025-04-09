def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	if not a or not a[0]:
		return -1
	rows= len(a)
	cols=len(a[0])
	b = [[a[row][col] for row in range(rows)] for col in range(cols)]

	return b