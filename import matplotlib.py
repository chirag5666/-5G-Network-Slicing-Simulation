import matplotlib.pyplot as plt
import numpy as np

# Time range
time = np.linspace(0, 10, 100)

# Simulated bandwidth utilization
traditional_system = 60 + 5 * np.sin(0.6 * time)  # Example sine wave function for a traditional system
ai_driven_system = 85 + 5 * np.sin(0.4 * time)    # Example sine wave function for an AI-driven system

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(time, ai_driven_system, label="AI-Driven System", color="orange")
plt.plot(time, traditional_system, label="Traditional System", linestyle="--", color="gold")

# Adding labels and title
plt.title("Bandwidth Utilization Over Time", fontsize=16)
plt.xlabel("Time (arbitrary units)", fontsize=12)
plt.ylabel("Bandwidth Utilization (%)", fontsize=12)

# Adding legend
plt.legend()

# Display the grid
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
