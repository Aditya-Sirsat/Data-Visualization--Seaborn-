# Data Visualization Using Seaborn and Matplotlib

This project focuses on visualizing India's export and import data from 1997 to July 2022. By leveraging Seaborn and Matplotlib libraries, various plots are generated to uncover insights and trends in the dataset.

## Dataset

Source: [Exports and Imports of India](https://www.kaggle.com/datasets/ramjasmaurya/exports-and-imports-of-india19972022)

The dataset comprises India's export and import statistics over the years, including:

- Year
- Country
- Export Value
- Import Value
- Total Trade Value

## Visualizations

### 1. Trend of Exports and Imports Over Years

![alt text](<Plots and Graphs/line_exports_imports.png>)

A line chart depicting the annual trends of India's exports and imports. The visualization highlights periods of significant growth and decline, reflecting economic events and policy changes.

### 2. Top 10 Countries by Total Trade

![alt text](<Plots and Graphs/bar_top_trade.png>)

A bar plot showcasing the top 10 countries contributing to India's total trade. This visualization emphasizes the major trade partners and their respective shares.

### 3. Distribution of Export Values Across Countries

![alt text](<Plots and Graphs/box_exports.png>)

A box plot illustrating the spread of export values across different countries, with a zoomed-in y-axis to focus on the majority of data points, excluding extreme outliers.

### 4. Export vs Import

![alt text](<Plots and Graphs/scatter_exports_imports.png>)

A scatter plot comparing export and import values, revealing correlations and trade imbalances between countries.

### 5. Distribution of Export Values

![alt text](<Plots and Graphs/hist_trade_balance.png>)

A histogram displaying the frequency distribution of export values, highlighting the concentration of data points and the presence of outliers.

### 6. Export Value Density (Filtered)

![alt text](<Plots and Graphs/kde_total_trade.png>)

A Kernel Density Estimate (KDE) plot providing a smoothed representation of the export value distribution after filtering out extreme outliers.

### 7. Export Distribution Across Top Countries

![alt text](<Plots and Graphs/violin_imports.png>)

A violin plot combining aspects of box plots and KDEs to show the distribution of export values across the top countries, indicating variability and central tendency.

### 8. Top 10 countries by trade deficit

![alt text](<Plots and Graphs/bar_trade_deficit.png>)

A bar plot showcasing the top 10 countries by trade deficit. This visualization emphasizes the major trade partners and their respective in trade deficit.

### 9. Top 10 countries by trade surplus

![alt text](<Plots and Graphs/bar_trade_surplus.png>)

A bar plot showcasing the top 10 countries by trade surplus. This visualization emphasizes the major trade partners and their respective shares in trade surplus.

### 10. Exports Share by Top 8 Countries

![alt text](<Plots and Graphs/pie_exports_share.png>)

A pie (ring) chart depicting the share of total exports contributed by the top 8 countries, with the "Others" category representing the remaining countries.

## Technologies Used 

- **Python** – A versatile programming language used for data analysis and visualization.  
- **Pandas** – A powerful library for data manipulation and handling structured datasets.  
- **Seaborn** – A statistical data visualization library built on top of Matplotlib for creating attractive plots.  
- **Matplotlib** – A plotting library for creating static, animated, and interactive visualizations in Python.  


## Files Included

- `data_visualization.py`: Python script containing the code for data visualization.
- `exports and imports of india(1997- July 2022) - exports and imports.xlsx`: Excel file with the dataset.
- `README.md`: Project documentation.

## Insights

- **Trade Growth**: The line charts reveal periods of significant growth and decline in India's trade, correlating with global economic events.
- **Major Trade Partners**: The bar plot identifies key countries contributing to India's trade, emphasizing the importance of these relationships.
- **Export Distribution**: The box and violin plots illustrate the variability in export values across countries, highlighting both consistency and outliers.
- **Trade Imbalances**: The scatter plot indicates correlations and imbalances between exports and imports, suggesting areas for policy focus.

