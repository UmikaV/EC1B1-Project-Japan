# %%
# Import dataset of variables for Japan into Python
import pandas as pd

# Allow the python to access the downloads file to access the relevant data for Japan
japan_file = '/Users/umikavekaria/Documents/GitHub/EC1B1-Group-42/International_Financial_Statistics_Japan.xlsx'

# Allow the python to access the downloads file to access the relevant data for US
us_file = '/Users/umikavekaria/Documents/GitHub/EC1B1-Group-42/International_Financial_Statistics_US.xlsx'

# Load these files into a Panda DataFrame
japan_df = pd.read_excel(japan_file)
us_df = pd.read_excel(us_file)

# Merge the two datasets together in Python
merged_df = pd.concat([japan_df, us_df], axis=1)
print(merged_df)



