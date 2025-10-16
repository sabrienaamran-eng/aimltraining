import datetime
import inspect
dtclassess=inspect.getmembers(datetime,inspect.isclass)

print('All Classes in datetime module')
for n, func in dtclassess:
    print(n,end="\t")

print('\n ---Today---\n')
print(datetime.date.today())
print('\n ---Current Time---\n')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I %M %S %p')
print('Current Time',cttime)
print('Formated Time',formatedtime)