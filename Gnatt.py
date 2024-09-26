import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the tasks and their start and end dates
tasks = {
    "Write a draft of the conference paper": ["2024-10-15", "2024-10-21"],
    "Write the conference paper": ["2024-11-05", "2024-11-14"],
    "Reverse engineering lab": ["2024-10-11", "2024-10-16"],
    "Finalize the design": ["2024-09-27", "2024-10-02"],
    "Find motor and parts": ["2024-10-02", "2024-10-08"],
    "Manufacture parts": ["2024-10-05", "2024-10-16"],
    "Assemble the device": ["2024-10-16", "2024-10-19"],
    "Test and evaluate the device": ["2024-10-19", "2024-10-24"],
    "Make any changes if necessary": ["2024-10-24", "2024-10-28"],
    "Create video/poster": ["2024-10-28", "2024-11-01"],
    "Final presentation preparation": ["2024-11-01", "2024-11-08"]
}

# Convert the task dates to a DataFrame
df = pd.DataFrame(
    [(task, datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")) for task, (start, end) in tasks.items()],
    columns=["Task", "Start", "End"]
)

# Sort the DataFrame by start date
df = df.sort_values(by='Start', ascending=False)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Add grid lines with True
ax.grid(True)
# Create a bar for each task
for i, (task, start, end) in enumerate(zip(df['Task'], df['Start'], df['End'])):
    ax.barh(task, end - start, left=start, height=0.4, color='blue', edgecolor='black')

# Set x-axis limits to start from the first project's start date
ax.set_xlim(df['Start'].min(), df['End'].max())


# Add month labels at the start of each month
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))  
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))  # Show minor ticks for every day
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))  

# Adjust font size for major and minor ticks
ax.tick_params(axis='x', which='both', labelsize=6)  # Set the font size for both major and minor ticks

# Add month labels
for month in ['Oct', 'Nov']:
    ax.text(datetime(2024, 10, 1) if month == 'Oct' else datetime(2024, 11, 1), -0.5, month, 
            horizontalalignment='center', color='black', fontsize=10, fontweight='bold')

plt.xlabel('Dates')
plt.ylabel('Tasks')

plt.tight_layout()
plt.show()


