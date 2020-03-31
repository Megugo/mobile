import csv
cdr=[]
with open('data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		cdr.append(row)
cd=-20 
sn=0

for i in range(1,len(cdr)): 
	if '933156729' in cdr[i][cdr[0].index('msisdn_origin')]: 
		cd+=float(cdr[i][cdr[0].index('call_duration')]) 
		sn+=float(cdr[i][cdr[0].index('sms_number')]) 
print ("%.2f" % (cd*2 + sn*2))