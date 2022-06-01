from utils.settings import GlobalVariables

class Comment:
    def __init__(self, _id, _web, _cat, _isArti, _title, _txt, _uid, _pid, _ptitle, _ptxt, _puid, _time, _stxt):
        self.id = _id
        self.isArti = _isArti
        self.title = _title
        self.txt = _txt
        self.uid = _uid
        self.pid = _pid
        self.ptitle = _ptitle
        self.ptxt = _ptxt
        self.puid = _puid
        self.time = _time
        self.web = _web
        self.cat = _cat
        self.stxt = _stxt

    # @property
    # def getCId(self):
    #     return self.cId
    #
    # @property
    # def getCPid(self):
    #     return self.cPid
    #
    # @property
    # def getCTxt(self):
    #     return self.cTxt
    #
    # @property
    # def getUName(self):
    #     return self.uName
    #
    # @property
    # def getCTime(self):
    #     return self.cTime
    #
    # @property
    # def getCStxt(self):
    #     return self.cStxt

    def addToDf(self):
        # print(comment.getCTxt)
        # print(comment.getTime)

        GlobalVariables.__CDF__.loc[len(GlobalVariables.__CDF__.index)] = [self.id, self.web, self.cat, self.isArti, self.title, self.txt, self.uid
            , self.pid, self.ptitle, self.ptxt, self.puid, self.time, self.stxt]


