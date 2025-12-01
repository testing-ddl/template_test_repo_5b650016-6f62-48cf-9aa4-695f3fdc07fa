# Script accepts one argument which is the sleep time in seconds.  By default, it'll be 10s.

import sys
from datetime import datetime
import time
from random import random, seed
import json

TITLE = "My baseline Batch Job"
SLEEP = 3
NUM_METRICS = 3
SEED = datetime.now()

f_results = open("results.txt", "wt")

f_results.write(TITLE+"\n")
f_results.write("Start Time: " + str(datetime.now()) + "\n")
print("Start Time: " + str(datetime.now()))

if (len(sys.argv) > 1):
    sleep_time = int(sys.argv[1])
else:
    sleep_time = SLEEP

time.sleep(sleep_time)

f_results.write("Stop Time: " + str(datetime.now()) + "\n")
print("Stop Time: " + str(datetime.now()))

f_metrics = open("dominostats.json", "wt")

d_metrics = {}
d_metrics["seed"] = str(SEED)
seed(SEED)

for i in range(NUM_METRICS):
    d_metrics["m"+str(i)] =  random()

f_metrics.write(json.dumps(d_metrics))

f_email = open("email.html", "wt")
f_email.write("<h1>" + TITLE + "</h1>\n")
for item in d_metrics.items():
    f_email.write("<ul>\n")
    f_email.write("<li>" + str(item[0]) + ": " + str(item[1]) + "</li>\n")
    f_email.write("</ul>")

print("Completed at: " + str(datetime.now()))
