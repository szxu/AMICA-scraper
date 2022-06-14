from utils.settings import GlobalVariables
import pandas as pd

class DfHandler():
    @staticmethod
    def make_comment_df():
        df = pd.DataFrame([], columns=list(["ID",
                                            "Website",
                                            "Category",
                                            "Is Article",
                                            "Comment Title",
                                            "Comment Text",
                                            "User ID",
                                            "Parent ID",
                                            "Parent Title",
                                            "Parent Text",
                                            "Parent User ID",
                                            "Time",
                                            "Segmented Text"]))

        return df

    @staticmethod
    def make_news_df():
        # df = pd.DataFrame([], columns=list(["ID",
        #                                     "Website",
        #                                     "Category",
        #                                     "News Title",
        #                                     "News Text",
        #                                     "Source",
        #                                     "Comment Time",
        #                                     "Segmented Text"]))

        df = pd.DataFrame({"ID":[],"Website":[],
                                            "Category":[],
                                            "News Title":[],
                                            "News Text":[],
                                            "Source":[],
                                            "Time":[],
                                            "Segmented Text":[]})
        return df

    @staticmethod
    def update_parent():
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

    @staticmethod
    def get_ids(df):
        return df.ID.values.tolist()

    @staticmethod
    def append_df(df1, df2):
        print(df1)
        print("=" * 20)
        print(df2)
        return pd.concat([df1, df2], join="inner")




