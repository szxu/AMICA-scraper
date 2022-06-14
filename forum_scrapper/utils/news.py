class News:
    def __init__(self, _id, _web, _cat, _title, _txt, _source, _time, _stxt):
        self.id = _id
        self.web = _web
        self.cat = _cat
        self.title = _title
        self.txt = _txt
        self.source = _source
        self.time = _time
        self.stxt = _stxt

    def add_row(self, running_df):
        running_df.loc[len(running_df.index)] = [self.id, self.web, self.cat, self.title, self.txt, self.source
            , self.time, self.stxt]
        return running_df