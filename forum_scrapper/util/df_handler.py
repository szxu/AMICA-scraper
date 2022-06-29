import pandas as pd

class DfHandler():
    @staticmethod
    def make_comment_df():
        df = pd.DataFrame({"ID": [],
                           "Website": [],
                           "Category": [],
                           "Is Article": [],
                           "Comment Title": [],
                           "Comment Text": [],
                           "User ID": [],
                           "Parent ID": [],
                           "Parent Title": [],
                           "Parent Text": [],
                           "Parent User ID": [],
                           "Time": [],
                           "Segmented Text": []})

        return df

    @staticmethod
    def make_news_df():
        df = pd.DataFrame({"ID":[],"Website":[],
                                            "Category":[],
                                            "News Title":[],
                                            "News Text":[],
                                            "Source":[],
                                            "Time":[],
                                            "Read Count": [],
                                            "Segmented Text":[]})
        return df

    @staticmethod
    def get_ids(df):
        return df.ID.values.tolist()

    @staticmethod
    def append_df(df1, df2):
        print(df1)
        print("=" * 20)
        print(df2)
        frames = [df1, df2]
        return pd.concat(frames)

    @staticmethod
    def update_parent(source):
        df = source

        for idx in source.index:
            try:
                if str(source["Is Article"][
                           idx]) == 'False':  # and pd.isnull(settings.__CDF__["Parent Text"][idx]) is True:
                    pRow = df.loc[lambda df: df["ID"] == source["Parent ID"][idx]]
                    source["Parent Title"][idx] = df.loc[pRow.index]["Comment Title"].values[0]
                    source["Parent Text"][idx] = df.loc[pRow.index]["Comment Text"].values[0]
                    source["Parent User ID"][idx] = df.loc[pRow.index]["User ID"].values[0]
                    print("Finish Update Comment" + idx)
            except:
                continue

        return source



    @staticmethod
    def update_link(df):
        def remove_comment_from_link(str):
            strs = str.split('/comment_')
            return strs[0]


        web_name = df['Website'][0]
        cat_name = df['Category'][0]

        if web_name == 'WXC':
            if cat_name == 'morenews':
                df['link'] = 'https://www.wenxuecity.com/news/' + df['ID'].apply(remove_comment_from_link) + '.html'
        elif web_name == 'MIT':
            df['link'] = 'https://www.mitbbs.com/article/' + cat_name + '/' + df['ID'].astype(str) + '_3.html'

        return df

    @staticmethod
    def update(df):
        df = DfHandler.update_parent(df)
        df = DfHandler.update_link(df)
        return df


# if __name__ == '__main__':
#     path = '/home/ktonxu/project/coen493/Misinfo Analysis/forum_scrapper/files/forum/MIT/MIT_USANews_2022-06-19_2022-06-19.csv'
#     df = pd.read_csv(path)
#     try:
#         df = DfHandler.update_link(df)
#     except Exception as ex:
#         print(ex)
#
#     df.to_csv(path, index=False)

