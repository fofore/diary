import os
import time

year = time.strftime("%Y")
month = time.strftime("%m")
day = time.strftime("%d")

#print year,month,day


if not os.path.exists(year):
	os.mkdir(year)

os.chdir(year)
#print os.getcwd()

if not os.path.exists(month):
	os.mkdir(month)

os.chdir(month)
#print os.getcwd()

if os.name is "nt":
    os.system("gvim %s.md"%(day))
else:
	os.system("vim %s.md"%(day))
