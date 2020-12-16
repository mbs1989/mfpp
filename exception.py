from functions import *


a = 5
b = 2

"""
try:
    # my execution
except:
    # catch exception and tell the system what do if error happens
    """


try:
    x = division(a,b)
    print("le résultat est ",x)
except Exception as myexcept:
    print("quelque chose se passe mal et mon exception est de type", myexcept.__class__)
else:
    print("le programme se termine")
