from utils.settings import GlobalVariables
import pandas as pd

class Comment:
    def __init__(self, _id, _web, _cat, _isArti, _title, _txt, _uid, _pid, _ptitle, _ptxt, _puid, _time, _stxt):
        self.id = _id
        self.web = _web
        self.cat = _cat
        self.isArti = _isArti
        self.title = _title
        self.txt = _txt
        self.uid = _uid
        self.pid = _pid
        self.ptitle = _ptitle
        self.ptxt = _ptxt
        self.puid = _puid
        self.time = _time
        self.stxt = _stxt

    def add_row(self, running_df):
        running_df.loc[len(running_df.index)] = [self.id, self.web, self.cat, self.isArti, self.title, self.txt, self.uid
            , self.pid, self.ptitle, self.ptxt, self.puid, self.time, self.stxt]
        return running_df

    def print_comment(self):
        print([self.id, self.web, self.cat, self.isArti, self.title, self.txt, self.uid
            , self.pid, self.ptitle, self.ptxt, self.puid, self.time, self.stxt])
