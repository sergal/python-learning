def accepts(*types):
    def check(f):
        def tmp(*args):

            accepted = True
            for arg in args:
                acceptedlist = map(lambda x: isinstance(arg, x), types)
                if not True in acceptedlist:
                    accepted = False
                    break

            if accepted:
                print "acceped"
                return f(*args)
            else:
                print "not accepted"
                return None

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

            if accepted:
                print "good return"
                return res
            else:
                print "bad return"
                return None

        return tmp

    return check