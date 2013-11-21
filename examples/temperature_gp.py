M = gp.Mean(lambda x: temps_2010.mean())

C = gp.Covariance(matern.euclidean,
            diff_degree=0.5,
            scale=20,
            amp=6)

# Observe some data
gp.observe(M, C, obs_mesh = range(len(temps_2010)),
        obs_vals = temps_2010, obs_V = 20)

xmesh = np.linspace(0, len(temps_2010))
gp.plot_envelope(M, C, xmesh)

for i in range(3):
    f = gp.Realization(M, C)
    plt.plot(xmesh, f(xmesh))

plt.plot(range(len(temps_2010)), temps_2010, 'k.', markersize=4)
plt.tight_layout()