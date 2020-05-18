from num2t4ru import num2text
from docxtpl import DocxTemplate
import csv
from docx2pdf import convert
def mob():
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
    return ("%.0f" % (cd*2 + sn*2))

def internet():
    cdr = []
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
        # if (cdr[i][2])!='0.000':
        time.append(int(float(cdr[i][2])))
        weight.append((float(cdr[i][12])) / (2 ** 20))
        bytes += float(cdr[i][12])
    bytes = bytes / (2 ** 10)
    if bytes > 1000:
        price = (bytes - 1000) * 0.5
    return("%.0f" % price)

male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
mobile_price = int(mob())
internet_price = int(internet())
full_price = mobile_price+internet_price
ndc = "%.0f" % (full_price*0.2)
doc = DocxTemplate("blank.docx")
context ={
    'mobile' : mobile_price,
    'internet' : internet_price,
    'full' : full_price,
    'ndc' : ndc,
    'str_price' : (num2text(full_price, male_units))
}
doc.render(context)
doc.save("bill.docx")
convert("bill.docx")