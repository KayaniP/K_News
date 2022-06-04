class States:
    def __init__(self, id, uf, name, flag):
        self.id = id
        self.uf = uf
        self.name = name
        self.flag = flag
        self.list = []
    
    def get_id(self):
        return self.id
    def get_uf(self):
        return self.uf
    def get_name(self):
        return self.name
    def get_flag(self):
        return self.flag
    def set_news(self, news):
        self.list = self.list + news     
    def get_news(self):
        return self.list

