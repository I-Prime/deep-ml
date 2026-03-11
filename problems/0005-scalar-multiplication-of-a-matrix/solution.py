def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [[ele* scalar for ele in row]for row in matrix]