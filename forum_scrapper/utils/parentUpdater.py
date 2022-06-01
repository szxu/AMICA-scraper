from utils.settings import GlobalVariables


class ParentUpdater():

    @staticmethod
    def init():
        df = GlobalVariables.__CDF__

        for idx in GlobalVariables.__CDF__.index:
            try:
                if str(GlobalVariables.__CDF__["Is Article"][
                           idx]) == 'False':  # and pd.isnull(settings.__CDF__["Parent Text"][idx]) is True:
                    pRow = df.loc[lambda df: df["Comment ID"] == GlobalVariables.__CDF__["Parent ID"][idx]]
                    GlobalVariables.__CDF__["Parent Title"][idx] = df.loc[pRow.index]["Comment Title"].values[0]
                    GlobalVariables.__CDF__["Parent Text"][idx] = df.loc[pRow.index]["Comment Text"].values[0]
                    GlobalVariables.__CDF__["Parent User ID"][idx] = df.loc[pRow.index]["User ID"].values[0]
            except:
                continue









