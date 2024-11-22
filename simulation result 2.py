# Latency simulation
traffic_spike = np.sin(np.linspace(0, 3 * np.pi, 100)) + 1.5
traditional_latency = 50 + 30 * traffic_spike  # Higher latency during spikes
ai_latency = 40 + 10 * traffic_spike          # Reduced latency with AI optimization

# Plot
plt.plot(time, traditional_latency, 'r--', label='Traditional System')
plt.plot(time, ai_latency, 'g-', label='AI-Driven System')

plt.title('Latency Comparison Under Dynamic Traffic')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Latency (ms)')
plt.legend()
plt.grid()
plt.show()
