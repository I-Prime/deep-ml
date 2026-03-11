import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape!=v2.shape:
		raise ValueError("make sure the arrays are of same length")
	if v1.size==0:
		raise  ValueError("Array cannot be empty")
	v1_flat=v1.flatten()
	v2_flat=v2.flatten()
	dot_product=np.dot(v1_flat,v2_flat)
	magnitude1=np.sqrt(np.sum(v1_flat**2))
	magnitude2=np.sqrt(np.sum(v2_flat**2))

	if magnitude1==0  or magnitude2==0:
		raise ValueError("Vectors cannot be of zero length")
	return round(dot_product/(magnitude1*magnitude2),4)