import numpy as np
import matplotlib.pyplot as plt

# Data arrays for each person
stella = np.array([5, 5, 5, 4, 5, 5, 5, 5])
arden = np.array([4, 2, 5, 5, 5, 5, 5, 4])
safia = np.array([4, 3, 2.5, 2, 4.5, 5, 4, 3.5])
joey = np.array([4, 4, 5, 4.5, 4, 4, 5, 5])
summit = np.array([4, 3, 5, 5, 5, 3, 5, 5])

# Combining all arrays into one
data = np.array([stella, arden, safia, joey, summit])

# Calculating mean and standard deviation
mean_values = np.mean(data, axis=0)
std_dev_values = np.std(data, axis=0)

# Category labels
labels = ['Ease', 'Frequency', 'Navigation', 'Ability', 'Time', 'Look', 'Content', 'Organization']

# Printing the mean and standard deviation values
print("Mean and Standard Deviation for Each Category:")
for i, label in enumerate(labels):
    print(f"{label:<12} : Mean = {mean_values[i]:<4.2f}, Standard Deviation = {std_dev_values[i]:<4.2f}")

# Defining contrasting colors for the bar graphs
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Reducing the font size for the x-axis labels to a quarter of the original size
x_axis_font_size = 5

# Plotting the bar graph for individual ratings with reduced font size
plt.figure(figsize=(14, 6))
plt.subplot(1, 3, 1)  # 1st subplot

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

plt.bar(x - 2*width, stella, width, color=colors[0], label='Stella')
plt.bar(x - width, arden, width, color=colors[1], label='Arden')
plt.bar(x, safia, width, color=colors[2], label='Safia')
plt.bar(x + width, joey, width, color=colors[3], label='Joey')
plt.bar(x + 2*width, summit, width, color=colors[4], label='Summit')

plt.xlabel('Categories')
plt.ylabel('Ratings')
plt.title('Individual Ratings')
plt.xticks(x, labels, fontsize=x_axis_font_size)
plt.legend()

# Plotting the bar graph for means with reduced font size
plt.subplot(1, 3, 2)  # 2nd subplot
plt.bar(labels, mean_values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Mean Rating')
plt.title('Mean Ratings by Category')
plt.xticks(fontsize=x_axis_font_size)

# Plotting the bar graph for standard deviations with reduced font size
plt.subplot(1, 3, 3)  # 3rd subplot
plt.bar(labels, std_dev_values, color='lightgreen')
plt.xlabel('Categories')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviations by Category')
plt.xticks(fontsize=x_axis_font_size)

# Adjusting layout and displaying the graphs
plt.tight_layout()
plt.show()
