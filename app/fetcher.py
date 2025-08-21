from get_data import GetData
import pandas as pd

class Fetcher:

    get_data = GetData()

    def get_df(self):
        return pd.DataFrame(list(self.get_data.get_collection()))

a = Fetcher()

print(a.get_df())