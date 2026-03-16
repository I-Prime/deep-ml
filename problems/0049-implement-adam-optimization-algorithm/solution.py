import numpy as np

def adam_optimizer(f, grad_func, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    # 1. Initialize parameters and state
    x = np.array(x0, dtype=float)
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    
    for t in range(1, num_iterations + 1):
        # 2. Compute the gradient at current position
        g = grad_func(x)
        
        # 3. Update biased moment estimates
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g**2)
        
        # 4. Compute bias-corrected estimates
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        
        # 5. Update parameters
        x = x - (learning_rate * m_hat) / (np.sqrt(v_hat) + epsilon)
        
    return x