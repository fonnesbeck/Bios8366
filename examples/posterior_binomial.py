fig, axes = plt.subplots(2, 2, sharex=True)

theta_vals = np.linspace(0, 1, 10000)

posterior = lambda theta, n, y: theta**y * (1-theta)**(n-y)

for i, ax in enumerate(axes.ravel()):
    ax.plot(theta_vals, posterior(theta_vals, n[i], y[i]))

plt.tight_layout()