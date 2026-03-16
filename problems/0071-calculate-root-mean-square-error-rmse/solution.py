
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	if y_true.shape!=y_pred.shape:
		raise ValueError("Arrays must be of equal length")
	if y_true.shape==0:
		raise ValueError("Array canont be  empty")
	rmse_res=np.sqrt(np.mean((y_true-y_pred)**2))	
	return round(rmse_res,3)
