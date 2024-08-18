import os, sys
os.system("git pull")
try:
    __import__("enc").MainMenu()
except Exception as e:
    exit(str(e))