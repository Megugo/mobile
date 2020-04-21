import csv
import matplotlib.pyplot as plot

cdr=[]
bytes = 0
price = 0
time = []
weight = []
with open('dump.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		if '192.168.250.3' in row:
			cdr.append(row)
for i in range(len(cdr)):
	#if (cdr[i][2])!='0.000':
	time.append(int(float(cdr[i][2])))
	weight.append((float(cdr[i][12]))/(2**20))
	bytes += float(cdr[i][12])
bytes = bytes/(2**10)
if bytes > 1000:
	price = (bytes-1000)*0.5
print("%.2f" % price)
buff1 = int(0)
buff2 = float(0)
for i in range(len(time)-1):
		for j in range(len(time)-i-1):
			if weight[j] > weight[j+1]:
				buff1 = weight[j]
				buff2 = time[j]
				weight[j] = weight[j+1]
				time[j] = time[j+1]
				weight[j+1] = buff1
				time[j+1] = buff2
print(time[len(time)-1])
print(weight[len(time)-1])
assert len(time) == len(weight)
plot.plot(weight,time)
plot.grid()
plot.show()
