data = [norm, norm_resample,  logn, logn_resample, expon, expon_resample,
        gumb, gumb_resample, tri, tri_resample]

fig, ax1 = plt.subplots(figsize=(10,6))
fig.canvas.set_window_title('Bootstrap sample boxplots')
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)


box_colors = ['darkkhaki','royalblue']

bp = plt.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
plt.setp(bp['boxes'][::2], color=box_colors[0])
plt.setp(bp['boxes'][1::2], color=box_colors[1])
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a faint horizontal grid to the plot
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
              alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Comparison of IID Bootstrap Resampling Across Five Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')

# Set the axes ranges and axes labels
ax1.set_xlim(0.5, len(data)+0.5)
top = 40
bottom = -5
ax1.set_ylim(bottom, top)
xtickNames = plt.setp(ax1, xticklabels=np.repeat(random_dists, 2))
plt.setp(xtickNames, rotation=45, fontsize=8)

# Legend
plt.figtext(0.80, 0.08,  str(N) + ' Random Numbers' ,
           backgroundcolor=box_colors[0], color='black', weight='roman',
           size='x-small')
plt.figtext(0.80, 0.045, 'IID Bootstrap Resample',
backgroundcolor=box_colors[1],
           color='white', weight='roman', size='x-small')