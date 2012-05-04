class DictAttr(dict):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError

class XDictAttr(DictAttr):

    def __getitem__(self, key):
        if key in self.keys():
            return super(XDictAttr, self).__getitem__(key)
        else:
            f_name = 'get_' + key
            if hasattr(self, f_name):
                return getattr(self, f_name)()
            else:
                raise KeyError

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default