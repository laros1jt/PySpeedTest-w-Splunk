import time
import datetime
import os
import sys

cmd = 'pyspeedtest'
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print (timestamp)
os.system(cmd)


