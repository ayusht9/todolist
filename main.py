import mysql.connector as ms
from datetime import datetime
from tabulate import tabulate
import os,time,platform

print(f'Greetings! {os.getlogin()}')
print(time.ctime())
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n')


mydb=ms.connect(host="localhost",user="rayon",password="cc",database='agenda') 
cursor=mydb.cursor()

def ins():
	L=[]
	name=input('Task name: ')
	L.append(name)

	temp = eval(input('Enter datetime: '))
	date = temp.strftime('%Y-%m-%d %H:%M:%S')
	L.append([date])

	place=input("Place: ")
	L.append(place)

	sql='insert into month1(name,time,place) values(%s,%s,%s)'
	cursor.execute(sql,(name,date,place))
	mydb.commit()

def dis():
	head=['status','task','tminus','place']
	cursor.execute("select tid,status,name,timediff(time,now()),place from month1")
	rec=cursor.fetchall()
	for i in [rec]:
	    print(tabulate(i,head,tablefmt="pretty"))

def mark():
	tid=input('Enter tid to be marked: ')
	cursor.execute("update month1 set status='COMPLETED' where tid={}".format(tid))
	mydb.commit()

def Del():
	tid=input('Enter tid to be deleted: ')
	cursor.execute("delete from month1 WHERE tid={}".format(tid))
	mydb.commit()

while True:
	dis()

	time.sleep(0.75)
	print("1. Add a task")
	print("2. Mark as completed")
	print("3. Delete a task")
	print("4. Exit")

	op = int(input('\noption « '))

	if(platform.system()=='Windows'):
		print(os.system('cls'))
	else:
	    print(os.system('clear'))

	time.sleep(0.5)

	if op == 1:
		ins()
	elif op == 2:
		mark()
	elif op == 3:
		Del()
	else:
		print('Have a nice day! :)')
		time.sleep(0.35)
		mydb.close()
		exit()