#!/usr/bin/env python3
# coding: latin-1
MSG = bytes(r"""
      �SX��>c`h��*�����7K���:푣������eשG<���-I7,��]Q���*Y�u�.�w�~ǤWfjݩ���P��m~t��KO\�A��ĊS��*�gyL�H��g�t��|1W�
""", "latin-1")
from hashlib import sha256
print(sha256(MSG).hexdigest())

if MSG[85] == 0x0B:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")
