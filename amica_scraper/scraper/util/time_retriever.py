from datetime import datetime

class Date_retriever():

    @staticmethod
    def retrieve_date(str):
        onlynumber = ''.join([i for i in str if i.isdigit()])
        year = onlynumber[0:4]
        month = onlynumber[4:6]
        day = onlynumber[6:8]
        hour = onlynumber[8:10]
        minute = onlynumber[10:12]
        second = onlynumber[12:14]

        timestamp = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

        return timestamp

# if __name__ == '__main__':
#     print(Date_retriever.retrieve_date("2017年02月06日02:30:33 "))