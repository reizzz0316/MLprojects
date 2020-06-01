import numpy as np 
import pandas as pd 
import pdb

user_df = pd.read_csv('../data/processed_data/user_df.data')

# There are '\\N' in product_id and industry columns, replace them with 0
user_df.replace('\\N', 0, inplace=True)

