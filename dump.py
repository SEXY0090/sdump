import os, sys
try:
    __import__("dump").main()
except Exception as e:
    exit(str(e))