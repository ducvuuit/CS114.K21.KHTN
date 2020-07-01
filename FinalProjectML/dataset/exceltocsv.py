import pandas as pd
data_xls = pd.read_Excel('data-label.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('your_csv.csv', encoding='utf-8')