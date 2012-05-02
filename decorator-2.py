import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Function time: %f" % (time.time()-t)
        return res

    return tmp