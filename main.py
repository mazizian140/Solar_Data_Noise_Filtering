#  Implement a noise filtering algorithm to enhance the signal from solar data.

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Sample 2D solar data (simulated for demonstration)
np.random.seed(0)
data = np.random.normal(100, 20, size=(100, 100))  # noisy solar data

# Apply Gaussian filtering to reduce noise
filtered_data = gaussian_filter(data, sigma=2)

# Visualize the original and filtered data
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Data (Noisy)")
plt.imshow(data, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Filtered Data")
plt.imshow(filtered_data, cmap='gray')
plt.show()

