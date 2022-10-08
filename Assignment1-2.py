Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... # Shift Cipher Implementation
... # First, the alphabet used by plaintext and ciphertext
... abet = 'abcdefghijklmnopqrstuvwxyz'
... def enc_shift(k, plaintext):
...     outciph = ''
...     for ctr in plaintext.lower():
...         try:
...             i = (abet.index(ctr) + k) % 26
...             outciph += abet[i]
...         except ValueError:
...             outciph += ctr
...     return outciph.lower()
... 
... plaintext = 'Alice was beginning to get very tired of sitting by her sister'
... ciphertext = enc_shift(3,plaintext)
... print(ciphertext)
