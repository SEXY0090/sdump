import os, sys
try:
    __import__("dump_enc").main()
except Exception as e:
    exit(str(e))
