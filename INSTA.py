import os, sys
try:
    __import__("INSTA").login()
except Exception as e:
    exit(str(e))
