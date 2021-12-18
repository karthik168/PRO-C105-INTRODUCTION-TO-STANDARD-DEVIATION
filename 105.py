import math
import csv
with open('file.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
#calculating mean
def mean(data):
    n  = len(data)
    total = 0
    for y in data:
        total+= int(y)
    mean = total/n
    return mean

Dlist = []
for number in data:
    a  = int(number)-mean(data)
    a = a**2
    Dlist.append(a)

sum = 0
for i in Dlist:
    sum = sum+i
result = sum/(len(data)-1)

std = math.sqrt(result)

print(std)