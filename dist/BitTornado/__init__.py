product_name = 'BitTornado'
version_short = 'T-0.3.17'

version = version_short+' ('+product_name+')'
report_email = version_short+'@degreez.net'

from types import *
import hashlib
import time
try:
    from os import getpid
except ImportError:
    def getpid():
        return 1

mapbase64 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-'

_idprefix = version_short[0]
for subver in version_short[2:].split('.'):
    try:
        subver = int(subver)
    except:
        subver = 0
    _idprefix += mapbase64[subver]
_idprefix += ('-' * (6-len(_idprefix)))
_idrandom = [None]

def resetPeerIDs():
    try:
        f = open('/dev/urandom','r')
        x = f.read(20)
        f.close()
    except:
        x = ''

    l1 = 0
    t = time.perf_counter()
    while t == time.perf_counter():
        l1 += 1
    l2 = 0
    t = int(time.time()*100)
    while t == int(time.time()*100):
        l2 += 1
    l3 = 0
    if l2 < 1000:
        t = int(time.time()*10)
        while t == int(time.perf_counter()*10):
            l3 += 1
    x += ( repr(time.time()) + '/' + str(time.time()) + '/'
           + str(l1) + '/' + str(l2) + '/' + str(l3) + '/'
           + str(getpid()) )

    s = ''
    for i in hashlib.sha1(x.encode('utf-8')).digest()[-11:]:
        s += mapbase64[i & 0x3F]
    _idrandom[0] = s
        
resetPeerIDs()

def createPeerID(ins = '---'):
    assert type(ins) is str
    assert len(ins) == 3
    return _idprefix + ins + _idrandom[0]
