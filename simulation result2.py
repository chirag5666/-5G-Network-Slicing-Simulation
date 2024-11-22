import numpy as np
import matplotlib.pyplot as plt

# Time
time = np.linspace(0, 10, 100)

# Throughput (Mbps) for traditional system (fixed allocation)
traditional_embb = 70 * np.ones_like(time)
traditional_urllc = 50 * np.ones_like(time)
traditional_mmtc = 30 * np.ones_like(time)

# Throughput (Mbps) for AI-driven system (dynamic allocation)
ai_embb = 70 + 10 * np.sin(0.5 * time)
ai_urllc = 50 + 8 * np.sin(0.7 * time)
ai_mmtc = 30 + 12 * np.sin(0.4 * time)

# Plot
plt.plot(time, traditional_embb, 'r--', label='Traditional eMBB')
plt.plot(time, traditional_urllc, 'g--', label='Traditional URLLC')
plt.plot(time, traditional_mmtc, 'b--', label='Traditional mMTC')

plt.plot(time, ai_embb, 'r-', label='AI-Driven eMBB')
plt.plot(time, ai_urllc, 'g-', label='AI-Driven URLLC')
plt.plot(time, ai_mmtc, 'b-', label='AI-Driven mMTC')

plt.title('Slice-Specific Throughput Over Time')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Throughput (Mbps)')
plt.legend()
plt.grid()
plt.show()
