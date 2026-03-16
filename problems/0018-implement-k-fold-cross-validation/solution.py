import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = np.arange(n_samples)
    
    if shuffle:
        np.random.shuffle(indices)
    
    # 1. Determine the size of each fold
    # Using n_samples // k and adding 1 to the first few folds handles remainders
    fold_sizes = np.full(k, n_samples // k, dtype=int)
    fold_sizes[:n_samples % k] += 1

    # 2. Split indices into k folds
    current = 0
    folds = []
    for fold_size in fold_sizes:
        folds.append(indices[current:current + fold_size])
        current += fold_size

    # 3. Create the (train, test) pairs
    result = []
    for i in range(k):
        test_indices = folds[i].tolist()
        # Combine all other folds into the training set
        train_indices = np.concatenate([folds[j] for j in range(k) if i != j]).tolist()
        result.append((train_indices, test_indices))
    
    return result