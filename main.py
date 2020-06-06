import json
from rand import random #導入亂數函式

rndlist = []

for result in random(1000): #執行三十五次
  rndlist.append(result) #列印每次結果

with open("test.txt", "w") as jfile:
  for data in rndlist:
    jfile.write(str(data) + "\n")
print(rndlist)

rndlist = sorted(rndlist)
with open("json.txt", "w") as jfile:
  for data in rndlist:
    jfile.write(str(data) + "\n")
print(rndlist)