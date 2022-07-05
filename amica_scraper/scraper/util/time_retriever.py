

class Date_retriever():

    @staticmethod
    def retrieve_date(str):
        onlynumber = ''.join([i for i in str if i.isdigit()])
        year = onlynumber[0:4]
        month = onlynumber[4:6]
        date = onlynumber[6:8]

        return year, month, date

# if __name__ == '__main__':
#     print(Date_retriever.retrieve_date("2022-01-31"))