import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)   
    scores = scores - np.max(scores)    
    result = scores - np.log(np.sum(np.exp(scores)))    
    return np.round(result, 4)