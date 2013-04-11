import os
import time

year = time.strftime("%Y")
month = time.strftime("%m")
day = time.strftime("%d")
weekday = time.strftime("%a")
weeknum = time.strftime("%W")

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
    os.system("c:/vim/vim73/gvim %s-wk%s-%s.md"%(day, weeknum, weekday))
else:
    os.system("vim %s-wk%s-%s.md"%(day, weeknum, weekday))
