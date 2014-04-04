# This is the db p-key ID associated with actual Url.
dbId=12345678
# Base-58 -> Digits/letters
a='123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
baseCount=len(a)
print baseCount
enc=''

# Encoding algorithm.
# Encodes dbId into base58 hash
while dbId>=baseCount:
    div,mod=divmod(dbId,baseCount)
    enc = a[mod]+enc
    dbId = int(div)
enc = a[dbId]+enc
print "flic.kr/p/%s" % (enc,)
