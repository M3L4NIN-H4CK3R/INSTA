import os, sys
try:
    __import__("INSTA").login_kamu()
except Exception as e:
    exit(str(e))
