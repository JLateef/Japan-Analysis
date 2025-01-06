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

#Load revenue tax data
file_path = '/jlatee/data/public-sector_jpn.csv'
data = pd.read_csv(file_path)

# Filter for the relevant indicator
indicator_name = "Taxes on goods and services (% of revenue)"
filtered_data = data[data["Indicator Name"] == indicator_name]

# Ensure the Year column is numeric
filtered_data["Year"] = pd.to_numeric(filtered_data["Year"], errors='coerce')

# Sort by Year for proper trend plotting
filtered_data = filtered_data.sort_values("Year")

# Plot the trend
plt.figure(figsize=(10, 6))
plt.plot(filtered_data["Year"], filtered_data["Value"], marker='o', linestyle='-', label=indicator_name)
plt.title("Trend of Taxes on Goods and Services (% of Revenue) Over Time", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Taxes on Goods and Services (% of Revenue)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()



# Filter data starting from 1960
birth_data_file_path = '/jlatee/data/japan_birth_data_.csv'
population_since_1960 = population_data[population_data["year"] >= 1960]

# Plot population growth over time
plt.figure(figsize=(10, 6))
plt.plot(population_since_1960["year"], population_since_1960["population_total"], marker='o', linestyle='-', label="Population Total")
plt.title("Population Growth over time (1960 onwards", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Population", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()


#Extract data from World happiness report
happiness_file_path = '/jlatee/data/World_Happiness_Report2024.csv'
# Sort data for better visualization
sorted_generosity = average_scores.sort_values("Generosity", ascending=False)

# Bar plot for Generosity scores by country (first world
plt.figure(figsize=(12, 8))
plt.bar(sorted_generosity.index, sorted_generosity["Generosity"], color='skyblue')
plt.title("Generosity Comparison Among First-World Countries", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Generosity", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# Bar plot for Ladder scores by country (first world)
# Filter the dataset for first-world countries
first_world_data_new = new_happiness_data[new_happiness_data["Country name"].isin(first_world_countries)]

# Sort the data for visualization
sorted_ladder_scores = first_world_data_new.sort_values("Ladder score", ascending=False)

# Bar plot for Ladder scores by country
plt.figure(figsize=(12, 8))
plt.bar(sorted_ladder_scores["Country name"], sorted_ladder_scores["Ladder score"], color='skyblue')
plt.title("Ladder Score Comparison Among First-World Countries", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Ladder Score", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Pivot the data to create a matrix with years as rows and countries as columns. This is to generate happiness score over time.
happiness_pivot = first_world_happiness_data.pivot_table(
    index="year", 
    columns="Country name", 
    values="Life Ladder"
)

# Plot multiple lines for each first-world country's happiness score over time
plt.figure(figsize=(14, 8))
for country in happiness_pivot.columns:
    plt.plot(
        happiness_pivot.index, 
        happiness_pivot[country], 
        marker='o', linestyle='-', label=country
    )

plt.title("Happiness Score Over Time", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Ladder Score", fontsize=14)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#Bar plot for freedom to make life choices score by country
plt.figure(figsize=(12, 8))
plt.bar(sorted_ladder_scores["Country name"], sorted_ladder_scores["Ladder score"], color='skyblue')
plt.title("Freedom To Make Life Choices Comparison Among First-World Countries", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Freedom to make life choices", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



