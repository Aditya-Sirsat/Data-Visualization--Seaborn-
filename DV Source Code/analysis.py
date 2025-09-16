# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
file_path = "exports and imports of india(1997- July 2022) - exports and imports.xlsx"
df = pd.ExcelFile(file_path)
data = pd.read_excel(file_path, sheet_name=df.sheet_names[0])

# Drop rows with missing key values
data = data.dropna(subset=["Export", "Import", "Total Trade", "Trade Balance"])

# Create output folder
output_dir = "D:\\AI and Decentralization Internship\\Data Visualization (Seaborn)\\Plots and Graphs"
os.makedirs(output_dir, exist_ok=True)

# 1. Line plot - Exports vs Imports over years
plt.figure(figsize=(10,6))
yearly = data.groupby("Financial Year(start)").sum(numeric_only=True)
sns.lineplot(x=yearly.index, y=yearly["Export"], label="Exports")
sns.lineplot(x=yearly.index, y=yearly["Import"], label="Imports")
plt.title("India's Exports vs Imports Over Years")
plt.xlabel("Year")
plt.ylabel("Value (in millions USD)")
plt.legend()
plt.savefig(f"{output_dir}/line_exports_imports.png")
plt.close()

# 2. Bar plot - Top 10 countries by total trade
plt.figure(figsize=(10,6))
top_trade = data.groupby("Country")["Total Trade"].sum().nlargest(10)
sns.barplot(x=top_trade.values, y=top_trade.index, palette="Blues_r")
plt.title("Top 10 Countries by Total Trade")
plt.xlabel("Total Trade (in millions USD)")
plt.ylabel("Country")
plt.savefig(f"{output_dir}/bar_top_trade.png")
plt.close()

# 3. Bar Plot - Top 10 trade surplus countries
plt.figure(figsize=(10,6))
top_surplus = data.groupby("Country")["Trade Balance"].sum().nlargest(10)
sns.barplot(x=top_surplus.values, y=top_surplus.index, palette="Greens_r")
plt.title("Top 10 Trade Surplus Countries")
plt.xlabel("Trade Balance (in millions USD)")
plt.savefig(f"{output_dir}/bar_trade_surplus.png")
plt.close()

# 4. Bar Plot - Top 10 trade deficit countries
plt.figure(figsize=(10,6))
top_deficit = data.groupby("Country")["Trade Balance"].sum().nsmallest(10)
sns.barplot(x=top_deficit.values, y=top_deficit.index, palette="Reds_r")
plt.title("Top 10 Trade Deficit Countries")
plt.xlabel("Trade Balance (in millions USD)")
plt.savefig(f"{output_dir}/bar_trade_deficit.png")
plt.close()

# 5. Box plot - Exports
plt.figure(figsize=(8,6))
sns.boxplot(y=data["Export"], color="skyblue")
plt.title("Distribution of Exports Across Countries")
plt.savefig(f"{output_dir}/box_exports.png")
plt.close()

# 6. Violin plot - Imports
plt.figure(figsize=(8,6))
sns.violinplot(y=data["Import"], color="orange")
plt.title("Distribution of Imports Across Countries")
plt.savefig(f"{output_dir}/violin_imports.png")
plt.close()

# 7. Histogram - Trade Balance
plt.figure(figsize=(8,6))
sns.histplot(data["Trade Balance"], bins=50, kde=False, color="purple")
plt.title("Histogram of Trade Balance")
plt.xlabel("Trade Balance (in millions USD)")
plt.savefig(f"{output_dir}/hist_trade_balance.png")
plt.close()

# 8. KDE Plot - Total Trade
plt.figure(figsize=(8,6))
sns.kdeplot(x=pd.to_numeric(data["Total Trade"], errors="coerce").dropna(), fill=True, color="red")
plt.title("KDE Plot of Total Trade")
plt.xlabel("Total Trade (in millions USD)")
plt.savefig(f"{output_dir}/kde_total_trade.png")
plt.close()

# Scatter plot - Exports vs Imports
plt.figure(figsize=(8,6))
sns.scatterplot(x="Export", y="Import", data=data, alpha=0.5)
plt.title("Scatter Plot: Exports vs Imports")
plt.xlabel("Exports")
plt.ylabel("Imports")
plt.savefig(f"{output_dir}/scatter_exports_imports.png")
plt.close()

# Pie Chart
plt.figure(figsize=(8,8))
top_exports = data.groupby("Country")["Export"].sum().nlargest(8)
total_exports = data["Export"].sum()
others = total_exports - top_exports.sum()
pie_data = pd.concat([top_exports, pd.Series([others], index=["Others"])])
plt.pie(pie_data,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=140,
    wedgeprops=dict(width=0.4))
plt.title("Exports Share by Top 8 Countries")
plt.savefig(f"{output_dir}/pie_exports_share.png")
plt.close()

print("All charts saved in 'outputs' folder.")
