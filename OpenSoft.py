
import os

def openSofts(**kargs):
    for v in kargs.values():
        res = os.system(v)
        print(res)
