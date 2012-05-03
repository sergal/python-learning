import string

class Observable(object):

    def __init__(self, **kwargs):
         for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        attrs = [attr for attr in dir(self) if not attr.startswith('__')]
        m = map(lambda x: str(x) + "=" + str(getattr(self, x)), attrs)
        str_args = ", ".join(m)
        return self.__class__.__name__ + "(" + str_args + ")"        
