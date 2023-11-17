import numpy as np
arr = np.random.randint(1, 100, 10)
print((arr - np.min(arr)) / (np.max(arr) - np.min(arr)))