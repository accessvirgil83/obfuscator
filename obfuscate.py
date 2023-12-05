import base64
mycode = b"""
def rs(x):
    return list(map(ord,x))"""

secret = base64.b64encode(mycode)
mydecode = base64.b64decode(secret)
eval(compile(mydecode,'<string>','exec'))
