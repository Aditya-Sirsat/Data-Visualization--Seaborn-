# Data Visualization Using Seaborn

## Overview

This project focuses on visualizing India's export and import data from 1997 to July 2022. By leveraging Seaborn and Matplotlib libraries, various plots are generated to uncover insights and trends in the dataset.

## Dataset

The dataset comprises India's export and import statistics over the years, including:

- Year
- Country
- Export Value
- Import Value
- Total Trade Value

## Visualizations

### 1. Line Chart – Trend of Exports and Imports Over Years

A line chart depicting the annual trends of India's exports and imports. The visualization highlights periods of significant growth and decline, reflecting economic events and policy changes.

### 2. Bar Plot – Top 10 Countries by Total Trade

A bar plot showcasing the top 10 countries contributing to India's total trade. This visualization emphasizes the major trade partners and their respective shares.

### 3. Box Plot – Distribution of Export Values Across Countries (Zoomed-In)

A box plot illustrating the spread of export values across different countries, with a zoomed-in y-axis to focus on the majority of data points, excluding extreme outliers.

### 4. Scatter Plot – Export vs Import

A scatter plot comparing export and import values, revealing correlations and trade imbalances between countries.

### 5. Histogram – Distribution of Export Values

A histogram displaying the frequency distribution of export values, highlighting the concentration of data points and the presence of outliers.

### 6. KDE Plot – Export Value Density (Filtered)

A Kernel Density Estimate (KDE) plot providing a smoothed representation of the export value distribution after filtering out extreme outliers.

### 7. Violin Plot – Export Distribution Across Top Countries

A violin plot combining aspects of box plots and KDEs to show the distribution of export values across the top countries, indicating variability and central tendency.

### 8. Swarm Plot – Export Values by Country

A swarm plot displaying individual data points of export values across countries, offering a granular view of the data distribution.

### 9. Line Chart – Annual Export Growth Rate

A line chart illustrating the year-over-year percentage change in total exports, highlighting periods of rapid growth or decline.

### 10. Pie/Ring Chart – Exports Share by Top 8 Countries

A pie (ring) chart depicting the share of total exports contributed by the top 8 countries, with the "Others" category representing the remaining countries.

## Technologies Used

- Python
- Pandas
- Seaborn
- Matplotlib

## Files Included

- `data_visualization.py`: Python script containing the code for data visualization.
- `exports_imports_data.csv`: CSV file with the dataset.
- `README.md`: Project documentation.

## Insights

- **Trade Growth**: The line charts reveal periods of significant growth and decline in India's trade, correlating with global economic events.
- **Major Trade Partners**: The bar plot identifies key countries contributing to India's trade, emphasizing the importance of these relationships.
- **Export Distribution**: The box and violin plots illustrate the variability in export values across countries, highlighting both consistency and outliers.
- **Trade Imbalances**: The scatter plot indicates correlations and imbalances between exports and imports, suggesting areas for policy focus.

## Conclusion

This project demonstrates the power of data visualization in understanding complex datasets. By employing various plots, we can uncover trends, identify key players, and gain insights into India's trade dynamics.

## License

This project is licensed under the MIT License.
