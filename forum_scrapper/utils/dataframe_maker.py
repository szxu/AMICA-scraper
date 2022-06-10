import pandas as pd
from IPython.display import display

class DataFrameMaker():

    @staticmethod
    def make_comment_df():
        df = pd.DataFrame([], columns=list(["Comment ID",
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
                                                 "Comment Time",
                                                 "Segmented Text"]))

        return df