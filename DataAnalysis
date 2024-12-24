# The below is the analysis for graphing the central government debt

# Extract data for "Central government debt, total (% of GDP)" and year 
debt_trend_data = regression_data[['Central government debt, total (% of GDP)']].dropna() 
debt_trend_data['Year'] = debt_trend_data.index 

# Plot the trend over the years 
import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 6)) plt.plot(debt_trend_data['Year'], debt_trend_data['Central government debt, total (% of GDP)'], 
      marker='o', linestyle='-', linewidth=2) 

plt.title("Trend of Central Government Debt (% of GDP) Over Time", fontsize=14) 
plt.xlabel("Year", fontsize=12) 
plt.ylabel("Central Government Debt (% of GDP)", fontsize=12) 
plt.grid(True) 
plt.tight_layout() 
plt.show()
