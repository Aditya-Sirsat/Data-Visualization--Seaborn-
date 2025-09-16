# Drop rows with missing key values
data = data.dropna(subset=["Export", "Import", "Total Trade", "Trade Balance"])