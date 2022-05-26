import settings
import pandas as pd

class UpdateParent():
    def init(self):
        df = settings.__CDF__

        for idx in settings.__CDF__.index:
            try:
                if str(settings.__CDF__["Is Article"][
                           idx]) == 'False':  # and pd.isnull(settings.__CDF__["Parent Text"][idx]) is True:
                    pRow = df.loc[lambda df: df["Comment ID"] == settings.__CDF__["Parent ID"][idx]]
                    settings.__CDF__["Parent Title"][idx] = df.loc[pRow.index]["Comment Title"].values[0]
                    settings.__CDF__["Parent Text"][idx] = df.loc[pRow.index]["Comment Text"].values[0]
                    settings.__CDF__["Parent User ID"][idx] = df.loc[pRow.index]["User ID"].values[0]
            except:
                continue









