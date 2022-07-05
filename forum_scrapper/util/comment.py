import pandas as pd

class Comment:
    def __init__(self, _id, _web, _cat, _isarti, _title, _txt, _uid, _pid, _ptitle, _ptxt, _puid, _time, _stxt, _readcount, _replycount):
        self.id = _id
        self.web = _web
        self.cat = _cat
        self.isarti = _isarti
        self.title = _title
        self.txt = _txt
        self.uid = _uid
        self.pid = _pid
        self.ptitle = _ptitle
        self.ptxt = _ptxt
        self.puid = _puid
        self.time = _time
        self.stxt = _stxt
        self.readcount = _readcount
        self.replycount = _replycount

    def add_row(self, running_df):
        running_df.loc[len(running_df.index)] = [self.id, self.web, self.cat, self.isarti, self.title, self.txt, self.uid
            , self.pid, self.ptitle, self.ptxt, self.puid, self.time, self.stxt, self.readcount, self.replycount]
        return running_df

    def print_comment(self):
        print([self.id, self.web, self.cat, self.isarti, self.title, self.txt, self.uid
            , self.pid, self.ptitle, self.ptxt, self.puid, self.time, self.stxt, self.readcount, self.replycount])
