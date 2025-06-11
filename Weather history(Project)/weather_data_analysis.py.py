import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load dataset
a = pd.read_csv("D:\\PROJECTS\\Weather history(Project)\\weatherHistory.csv")

# Convert 'Formatted Date' to datetime format with UTC
a['Formatted Date'] = pd.to_datetime(a['Formatted Date'], utc=True) # UTC tells Pandas to convert all datetime values into the UTC time zone (Universal Coordinated Time) during parsing.

# Extract year, month, and day from the datetime column
a['Year'] = a['Formatted Date'].dt.year
a['Month'] = a['Formatted Date'].dt.month
a['Day'] = a['Formatted Date'].dt.day

# Rename column for simplicity
a.rename(columns={'Temperature (C)': 'Temp_C'}, inplace=True)

# Create 'charts' folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# 4. Monthly Temperature Analysis
grouped_month = a.groupby('Month')['Temp_C'].mean()
plt.figure(figsize=(10, 6))
plt.bar(grouped_month.index, grouped_month.values, color='c', width=0.5) # Acts grouped_month.index as x & grouped_month.values as y.
plt.title('Avg. Temperature in 12 Months')
plt.xlabel('Months', color='blue')
plt.ylabel('Temp (C)',color='b')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='both', color='red', linestyle='dotted')
plt.tight_layout()
plt.savefig('charts/monthly_temperature.png')
plt.show()

# 5. Yearly Temperature Trends
grouped_year = a.groupby('Year')['Temp_C'].mean()
plt.figure(figsize=(10, 6))
plt.bar(grouped_year.index, grouped_year.values, color='skyblue', width=0.5)
plt.grid(axis='both', color='r', linestyle='dotted')
plt.title('Average Temperature by Year', fontsize=14)
plt.xlabel('Year', color='b', fontsize=12)
plt.ylabel('Avg. Temp (°C)', color='b', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/yearly_temperature.png')
plt.show()

# 6. Extreme Temperature Days
max_temp = a['Temp_C'].max()
min_temp = a['Temp_C'].min()

hottest_day = a[a['Temp_C'] == max_temp]
coldest_day = a[a['Temp_C'] == min_temp]

print("\nHottest Day:")
print(hottest_day[['Formatted Date', 'Temp_C']].to_string(index=False)) # .to_string() :Converts DataFrame to clean string for display 

print("\nColdest Day:")
print(coldest_day[['Formatted Date', 'Temp_C']].to_string(index=False))

# 7. Weather Summary Analysis
top_5 = a['Summary'].value_counts().head(5)
e = [0.1, 0.03, 0.01, 0.009, 0.1]
c = ['purple', 'teal', 'hotpink', 'yellow', 'red']
plt.figure(figsize=(10, 6))
plt.pie(top_5, labels=top_5.index, explode=e, colors=c, shadow=True)
# top_5_summaries      	   Weather condition counts
# top_5_summaries.index	   The names of the top 5 conditions
plt.title('Top 5 Most Common Weather Conditions', fontsize=20, color='r')
plt.legend(
    top_5.index,
    title='Weather Condition',
    loc='upper right',
    bbox_to_anchor=(1.3, 1)
)
plt.tight_layout()
plt.savefig('charts/top5_weather_conditions.png')
plt.show()

# 8. Optional: Seasonal Analysis
season_map = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
}
a['Season'] = a['Month'].map(season_map)
seasonal_avg = a.groupby('Season')['Temp_C'].mean().reindex(['Winter', 'Spring', 'Summer', 'Autumn'])

plt.figure(figsize=(8, 6))
plt.bar(seasonal_avg.index, seasonal_avg.values, color='orange')
plt.title('Average Temperature by Season')
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('charts/seasonal_temperature.png')
plt.show()
