import numpy as np
import matplotlib.pyplot as plt

# combine the different collections into a list
# manipulate the following lines based on your data
data_to_plot = data
data_to_plot = data_to_plot.flatten()
data_to_plot = [data_to_plot]
#data_to_plot = data_to_plot.T

# Create a figure instance
fig, ax = plt.subplots()

def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value

parts = ax.violinplot(
        data_to_plot, showmeans=False, showmedians=False,
        showextrema=False)

for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

quartile1, medians, quartile3 = np.percentile(data_to_plot, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data_to_plot, quartile1, quartile3)])
whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax.vlines(inds, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)


# Create the boxplot
ax.set_xlabel('Heart rate', fontsize = 14)
ax.set_ylabel('Beats', fontsize = 14)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.show()
#plt.savefig("Heart_rate.png", dpi=1200)
