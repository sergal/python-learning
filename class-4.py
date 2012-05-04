class Meta(type):

    instance_list = []
    current = 0

    def __iter__(self):
        return self

    def next(self):
        if Meta.current >= len(Meta.instance_list):
            raise StopIteration
        else:
            Meta.current += 1
            return Meta.instance_list[Meta.current - 1]

class Req(object):
    __metaclass__ = Meta

    def __init__(self):
        Meta.instance_list.append(self)