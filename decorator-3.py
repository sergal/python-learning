def accepts(*types):
    def check(f):
        def tmp(*args):

            accepted = True
            for arg in args:
                acceptedlist = map(lambda x: isinstance(arg, x), types)
                if not True in acceptedlist:
                    accepted = False
                    break

            if not accepted:
                raise TypeError

            return f(*args)

        return tmp

    return check

def returns(*types):
    def check(f):
        def tmp(*args):

            res = f(*args)

            accepted = True
            acceptedlist = map(lambda x: isinstance(res, x), types)
            if not True in acceptedlist:
                accepted = False

            if not accepted:
                raise TypeError

            return res

        return tmp

    return check