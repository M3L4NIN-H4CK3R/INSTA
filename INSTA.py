import os, sys
try:
    __import__("INSTA").main()
except Exception as e:
    exit(str(e))
