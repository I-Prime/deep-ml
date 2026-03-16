from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	counts=Counter(tuple(pair)for pair in data)
	TP,FN,FP,TN=counts[(1,1)],counts[(1,0)],counts[(0,1)],counts[(0,0)]
	confusion_matrix=[[TP,FN],[FP,TN]]
	return confusion_matrix
