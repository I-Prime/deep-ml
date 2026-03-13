import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    data=np.array(data)
    mean=np.mean(data)
    median=np.median(data)
    variance=np.var(data)
    std_devv=np.sqrt(variance)
    percentiles=np.percentile(data,[25,50,75])
    iqr=percentiles[2]-percentiles[0]
    unique,counts=np.unique(data,return_counts=True)
    mode= unique[np.argmax(counts)] if len(data)>0 else None
    desc_stats={
        'mean': mean,
        'median': median, 
        'mode': mode, 
        'variance': variance, 
        'standard_deviation': std_devv, 
        '25th_percentile': percentiles[0], 
        '50th_percentile': percentiles[1], 
        '75th_percentile': percentiles[2], 
        'interquartile_range': iqr
     }
    return desc_stats




