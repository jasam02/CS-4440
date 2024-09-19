#!/usr/bin/python3
from pyroots import *
import hashlib
import sys
message = sys.argv[1]

#----------------------------------------------
h1 = hashlib.sha1()
h1.update(message.encode())
digest = h1.hexdigest()

padding = "0001" + "FF" + "00" + "3021300906052B0E03021A05000414" + digest + ("FF" * 217)

forged_sig, exactRoot = integer_nthroot(int(padding, 16), 3)
#----------------------------------------------

#Test Account: cs4440+u1281872+300.00

print(integer_to_base64(forged_sig))
