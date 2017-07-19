from datetime import datetime, timedelta
from sys import argv
#import pyximport

#pyximport.install()
import treematcher

if len(argv) > 1:
    num = int(argv[1])
else:
    num = 1

times = []

for i in range(0, num):
    startTime = datetime.now()

    treematcher.test()

    times += [datetime.now() - startTime]

total = sum(times, timedelta(0)) / len(times)
if (len(times) == 1):
    print "test: "
    print times[0]


print str(total)
