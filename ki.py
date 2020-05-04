#dbms
import mysql.connector
from mysql.connector import Error
print("this is rough ui of the project ")
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Vipul@kesari1',database='dbmsproject')
mycursor=mydb.cursor()
# mycursor.execute("show tables")
# for i in mycursor:
# 	print(i)
sql3="INSERT INTO soldiers (soldier_id,Name,Age,Gender,Address,Category,Post,Base_ID,Weapon_Allotted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "

sql = "INSERT INTO usercred (username,Urank,password) VALUES (%s, %s, %s)"
#Thak you function
def thank():
	print("Thank You for visiting our Database.")

# for query one
def query1():
	try:

		sql4="select * from base where Base_ID=%s"
		a=int(input("enter the base_id:"))
		val=(a,)
	
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
	#print(result[0])
	# print(result[1])
	# print(result[2])
	# print(result[3])
	# print(result[4])
	# print(result[5])
	# print(result[6])
	# print(result[7])
	# print(result[8])
		for i in result:
			print(i)
	except Exception as e:
		print(e)
	# else:
	# 	print("Data did not found!")

	#print("enter the base_id")
	finally:
		inp=input("Do you again want to see the details , yes/no:")
	if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
		civilianquery()
	elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
		thank()
	else:
		print("you selected wrong option!ooops")

	
# for query2 civilians
def query2():
	try:
		sql4="select Budget from base where Base_ID=%s"
		a=int(input("enter the base id which budget you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
	
#for query3 civilians
def query3():
	try:
		sql4="select Soldier_Count from base where Base_ID=%s"
		a=int(input("enter the base id which detail you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
		
	except Exception as e:
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
	
# for query 4 civilians
def query4():
	try:
		sql4="select Base_chief from base where Base_ID=%s"
		a=int(input("enter the base id which base chief name you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
		
	except Exception as e:
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
	
# for query 5 civilians
def query5():
	try:
		sql4="select SUM(Budget) from Base GROUP BY Category ORDER BY SUM(Budget) DESC"
		# a=int(input("enter the base id which base chief name you want to know:"))
		# val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)

	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
# for query 6 civilians
def query6():
	try:
		sql4="select chief,Category from defence"
		# a=int(input("enter the base id which base chief name you want to know:"))
		# val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	except Exception as e:
		print(e)

	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
# for query 7 civilians
def query7():
	try:
		sql4="select Vehicle_Type from vehicles where Base_ID=%s"
		a=int(input("enter the base id which detail you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	
	except Exception as e:
		print(e)

	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			civilianquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
		
# function for civilian queries
def civilianquery():
	print("press the following")
	print("enter 1 for details of the base")
	print("enter 2 for details of the  budget")
	print("enter 3 for details of the no of soldiers")
	print("enter 4 for details of the name of the chief")
	print("enter 5 for details of the total budget")
	print("enter 6 for details of the army chief")
	print("enter 7 for details of the no of vehicles")
	ab=int(input("enter the option:"))
	if(ab==1):
		query1()
	elif(ab==2):
		query2()
	elif(ab==3):
		query3()
	elif(ab==4):
		query4()
	elif(ab==5):
		query5()
	elif(ab==6):
		query6()
	elif(ab==7):
		query7()
	else:
		print("oops ! you entered the wrong option ! sorry !Try Again!")

	#print("enter 1 for details of the base")

	

#function for new user which is soldier
def armynewuser():
	print("Here your all details will be taken, Your name will work as your username ! and your soldier id will be your password.")
	sol_id=int(input("enter your soldier_id:"))
	name=input("enter your name:")
	age=int(input("enter your age:"))
	gender=(input("enter your gender: "))
	add=input("enter your address:")
	cat=input("enter your category:")
	post=input("enter your post:")
	B_id=int(input("enter your base_id:"))
	w_a=input("enter your Weapon_Alloted:")
	val=(sol_id,name,age,gender,add,cat,post,B_id,w_a)
	print("Renter your Base_id to validate your credentials")
	rB_id=int(input("Enter here your soldier_ID:"))
	if(sol_id==rB_id):
		mycursor.execute(sql3,val)
		mydb.commit()


		print("your account has created, run again the program to login!")
	else:
		print("your password verification failed! please try again! sorry!")


# function for existing user which is army official

def armyexistinguser():
	usern=(input("enter your username that is your name in the database:"))
	userp=int(input("enter your password that is your soldier_id:"))
	sql="select Name from soldiers where Name=%s"
	unm=(usern,)
	mycursor.execute(sql,unm)
	result=mycursor.fetchall()
	sql1="select Soldier_id from soldiers where Soldier_id=%s"
	upwd=(userp,)
	mycursor.execute(sql1,upwd)
	result1=mycursor.fetchall()

	c1=0
	for j in result1:
		c1=c1+1
	#k=result.count(logiid)
	#print(k)
	c=0
	for i in result:
		c=c+1

	if(c!=0 and c1!=0):
		print("login granted!")
		
		armyquery()

	else:
		print("your login credetials did not match please again enter the details for procedings!")



# function for new user which is civilian
def civiliannewuser():

	uname=(input("enter the email id:"))
	sli=uname[-10:len(uname)]
	if(sli=="@gmail.com"):
		rank="civilian"
		password=(input("enter the password:"))
		apassword=(input("verify password:"))
		val=(uname,rank,password)
		if(password==apassword):
			mycursor.execute(sql,val)
			mydb.commit()


			print("your account has created, run again the program to login!")
		else:
			print("your password verification failed! please try again! sorry!")
	else:
		print("you did not entered correct email id!")
		

# function for existing user which is civilian

def civilianexistinguser():
	logiid=(input("enter the email id:"))
	sli=logiid[-10:len(logiid)]
	if(sli=="@gmail.com"):
		lpassword=(input("enter the password:"))
		#sql="select uname,password from login where uname="+logiid+"and password="+lpassword
		sql="select username from usercred where username=%s"
		unm=(logiid,)
		mycursor.execute(sql,unm)
		result=mycursor.fetchall()
		sql1="select password from usercred where password=%s"
		upwd=(lpassword,)
		mycursor.execute(sql1,upwd)
		result1=mycursor.fetchall()

		c1=0
		for j in result1:
			c1=c1+1
		#k=result.count(logiid)
		#print(k)
		c=0
		for i in result:
			c=c+1

		if(c!=0 and c1!=0):
			print("login granted!")
			
			civilianquery()

		else:
			print("your login credetials did not match please again enter the details for procedings!")
	else:
		print("you entered wrong email id/ Or it was not ending with @gmail.com!")
		

def queries():
	print("enter the query to execute!")
	#sql=input("enter the query here :")
	mycursor.execute("Select Soldier_Count from Base where Base_ID = 1000")
	ans=mycursor.fetchall()
	for i in ans:
		print(i)

#function for armychiefquery 1
def armychiefquery1():
	try:
		sql4="select soldiers.Name, soldiers.soldier_id,weapons.Weapon_Name,weapons.Weapon_ID from soldiers, weapons where soldiers.Base_ID=weapons.Base_ID "
		#a=int(input("enter the base id which detail you want to know:"))
		#val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#army chief query 2
def armychiefquery2():
	try:
		sql4="select Name, soldier_id,Weapon_Name,Weapon_ID, from soldiers INNER JOIN weapons ON soldiers.Base_ID=weapons.Base_ID soldiers.Base_ID=%s"
		a=int(input("enter the base id which detail you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for amychief query 3
def armychiefquery3():
	try:
		sql4="select Base_ID,Soldier_Count from base ORDER BY Soldier_Count DESC"
		#a=int(input("enter the base id which detail you want to know:"))
		#val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# functionf or amychief query 4
def armychiefquery4():
	try:
		sql4="Select AVG(Budget) from Base"
		# a=int(input("enter the base id which detail you want to know:"))
		# val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#fucntion for armychief query 5
def armychiefquery5():
	try:
		sql4="Select Base_ID, Base_Chief, Attack_Count from Base ORDER BY Attack_Count"
		# a=int(input("enter the base id which detail you want to know:"))
		# val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for armychief query 6
def armychiefquery6():
	try:
		sql4="select * from development"
		# a=int(input("enter the base id which detail you want to know:"))
		# val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			armychiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")

# function for armychiefquery
def armychiefquery():
	print(" Hello Chief, Here are the commands which you can execute,Select any of the following command.")
	print("Enter 1. for getting details of th particular base")
	print("Enter 2. to Know which soldiers and Vehicles are present at a particular base ")
	print("Enter 3. to Know about base in descending order of population")
	print("Enter 4. to Know about the average budget of a base")
	print("Enter 5. to Display Base having Maximum number of Attacks ")
	print("Enter 6. to Display details of manufacturing weapons")
	n=int(input("Enter here :"))
	if(n==1):
		armychiefquery1()
	elif(n==2):
		armychiefquery2()
	elif(n==3):
		armychiefquery3()
	elif(n==4):
		armychiefquery4()
	elif(n==5):
		armychiefquery5()
	elif(n==6):
		armychiefquery6()
	else:
		print("ooops ! you selected wrong option!")
#fuction for base chief query 1
def basechiefquery1():
	try:
		sql4="INSERT INTO supply(Order_ID,Base_ID,Order_Cost,Purchase_Date,Delivery_Date) VALUES(%s,%s,%s,%s,%s)"
		a=int(input("Enter the order ID:"))
		b=int(input("Enter the base id:"))
		c=int(input("Enter the order cost:"))
		d=(input("Enter the puchase date:"))
		e=(input("Enter the Delivery_Date:"))
		val=(a,b,c,d,e)
		mycursor.execute(sql4,val)
		mydb.commit()
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			basechiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#function for base chief query 2
def basechiefquery2():
	try:
		sql4="INSERT INTO weapons(Weapon_ID,Base_ID,Weapon_Name,Weapon_Count,Weapon_Bullet_Count,Weapon_Type) VALUES(%s,%s,%s,%s,%s,%s)"
		a=int(input("Enter the weapon ID:"))
		b=int(input("Enter the base id:"))
		c=(input("Enter the weapon name:"))
		d=int(input("Enter the weapon count:"))
		e=int(input("Enter the Weapon_Bullet_Count:"))
		f=input("Enter the Weapon_Type: ")
		val=(a,b,c,d,e,f)
		mycursor.execute(sql4,val)
		mydb.commit()
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			basechiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for base chief query 3
def basechiefquery3():
	try:
		sql4="INSERT INTO vehicles(Vehicles_ID,Base_ID,Vehicle_Type,Vehicle_Capacity,Vehicle_Category) VALUES(%s,%s,%s,%s,%s)"
		a=int(input("Enter the Vehicles_ID ID:"))
		b=int(input("Enter the base id:"))
		c=(input("Enter the Vehicle_Type name:"))
		d=int(input("Enter the Vehicle_Capacity:"))
		e=(input("Enter the Vehicle_Category:"))
		#f=input("Enter the Weapon_Type: ")
		val=(a,b,c,d,e)
		mycursor.execute(sql4,val)
		mydb.commit()
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			basechiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
	

#fucntion for base chief query 4
def basechiefquery4():
	try:
		sql6="CREATE INDEX index_base ON base(Base_ID)"
		mycursor.execute(sql6)
		sql4="select count(*) from Transfer where Soldier_id in (select soldier_id from soldiers where Base_ID=%s)"
		a=int(input("enter the base id which detail you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			basechiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#function for base chief query 5
def basechiefquery5():
	try:
		sql4="INSERT INTO events(Base_ID,Event_Name) VALUES(%s,%s)"
		#a=int(input("Enter the weapon ID:"))
		b=int(input("Enter the base id:"))
		c=(input("Enter the event name:"))
		# d=int(input("Enter the weapon count:"))
		# e=int(input("Enter the Weapon_Bullet_Count:"))
		# f=input("Enter the Weapon_Type: ")
		val=(b,c)
		mycursor.execute(sql4,val)
		mydb.commit()
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			basechiefquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")

# function for baase chief
def basechiefquery():
	print(" Hello Base Chief !")
	print("You have the following option choose the followin.")
	print("Enter 1. to add new purchase to database.")
	print("Enter 2. to add new weapons in the database.")
	print("Enter 3. to add new vehicles in database.")
	print("Enter 4. to Know how many soldiers have applied for transfer from your base.")
	print("Enter 5. to Add an event into the database.")
	n=int(input("Enter here:"))
	if(n==1):
		basechiefquery1()
	elif(n==2):
		basechiefquery2()
	elif(n==3):
		basechiefquery3()
	elif(n==4):
		basechiefquery4()
	elif(n==5):
		basechiefquery5()
	else:
		print("you selected wrong option! ooops !")
#function for employe query 1
def employequery1():
	try:
		sql4="select * from Transfer where status='pending'"
		# a="pending"
		# val=(a,)
		mycursor.execute(sql4)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			employequery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#function for employe query 2
def employequery2():
	try:
		sql4="UPDATE Transfer set status='Accepted' where Transfer_ID=%s"
		#a=int(input("Enter the weapon ID:"))
		b=int(input("Enter the Transfer id:"))
		#c=(input("Enter the event name:"))
		# d=int(input("Enter the weapon count:"))
		# e=int(input("Enter the Weapon_Bullet_Count:"))
		# f=input("Enter the Weapon_Type: ")
		val=(b,)
		mycursor.execute(sql4,val)
		mydb.commit()
		print("Work Done!")
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		#sql="UPDATE soldiers Base_ID"
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			employequery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for employe query 3
def employequery3():
	try:
		sql4="UPDATE Transfer set status='Rejected' where Transfer_ID=%s"
		#a=int(input("Enter the weapon ID:"))
		b=int(input("Enter the transfer_id:"))
		#c=(input("Enter the event name:"))
		# d=int(input("Enter the weapon count:"))
		# e=int(input("Enter the Weapon_Bullet_Count:"))
		# f=input("Enter the Weapon_Type: ")
		val=(b,)
		mycursor.execute(sql4,val)
		mydb.commit()
		print("Work done!")
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			employequery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")

# function for employe query
def employequery():
	print(" Hello MR. employe")
	print(" Here are following option to choose")
	print("Enter 1. for viewing all the pending tansfers")
	print("Enter 2. for accepting transfer")
	print("Enter 3. for Rejecting Transfer")
	a=int(input("enter Here:"))
	if(a==1):
		employequery1()
	elif(a==2):
		employequery2()
	elif(a==3):
		employequery3()
	else:
		print("you entered wrong option")

#function for soldier query 1
def soldierquery1():
	try:
		sql4="INSERT INTO Transfer(Transfer_ID,Soldier_id,Name,From1,To,status) VALUES (%S,%S,%S,%S,%S,%S)"
		t_id=input("enter your transfer_id given by the chief:")
		sol_id=input("enter the soldier id :")
		name=input("enter your name:")
		currbase=input("enter your present Base:")
		tobase=input("where you want to go:")
		status="pending"
		val=(t_id,sol_id,name,currbase,tobase,status)



		#a=int(input("enter the base id which budget you want to know:"))
		mycursor.execute(sql4,val)
		mydb.commit()
		print("work done!")
		# result=mycursor.fetchall()
		# for i in result:
		# 	print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			soldierquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for soldier query 2
def soldierquery2():
	try:
		sql5="CREATE INDEX index_soldier ON soldiers(soldier_id) "
		mycursor.execute(sql5)
		sql4="select post from soldiers where soldier_id=%s"
		a=int(input("Enter yor soldier id:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			soldierquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for soldier query 3
def soldierquery3():
	try:
		sql4="select Weapon_Name,Weapon_Count from weapons where Base_ID=%s"
		sql10="select Weapon_Name,Weapon_Count from soldiers INNER JOIN weapons ON soldiers.Base_ID=weapons.Base_ID where Base_ID=%s"
		a=int(input("enter the base id which details you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			soldierquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
# function for soldier query 4
def soldierquery4():
	try:
		sql4="select Vehicle_Capacity from vehicles where Base_ID=%s"
		a=int(input("enter the base id which vehicles count you want to know:"))
		val=(a,)
		mycursor.execute(sql4,val)
		result=mycursor.fetchall()
		for i in result:
			print(i)
	#print("enter the ")
		
	
	except Exception as e :
		print(e)
	finally:
		inp=input("Do you again want to see the details , yes/no:")
		if(inp=="yes" or inp=="YES" or inp=="Yes" or inp=="Y" or inp=="y"):
			soldierquery()
		elif(inp=="no" or inp=="NO" or inp=="No" or inp=="N" or inp=="n"):
			thank()
		else:
			print("you selected wrong option!ooops")
#function for soldier query
def soldierquery():
	print("Hello Soldier ! Please Choose the option given below for further procedings!")
	print("Enter 1. for transfer .")
	print("Enter 2. for getting details about your post.")
	print("Enter 3. for getting weapons details in your base.")
	print("Enter 4. for getting vehicles details in your base.")
	data=int(input("Press Here Soldier:"))
	if(data==1):
		soldierquery1()
	elif(data==2):
		soldierquery2()
	elif(data==3):
		soldierquery3()
	elif(data==4):
		soldierquery4()
	else:
		print("you entered the wrong option")


# function for army official compilation
def armyquery():
	print("Hi , You guys are welcome at army login!")
	print("please ! enter your rank , soldier/base chief / army chief/employe")
	yo=input("enter here ! all letters in small!:")
	if(yo=="soldier" or yo=="Soldier" or yo=="SOLDIER"):
		soldierquery()
	elif(yo=="armychief"):
		armychiefquery()
	elif(yo=="basechief"):
		basechiefquery()
	elif(yo=="employe"):
		employequery()
	else:
		print("you entered wrong option! May be your fomat was wrong!")


# main function for running the code
print("press following")
print("enter 1. for the civilian :")
print("enter 2. for the army official")
a=int(input("press here:"))
if(a==1):
	print("1. for new user")
	print("2. for existing user")

	b=int(input("enter here :"))
	if(b==1):
		civiliannewuser()
	elif(b==2):
		civilianexistinguser()
	else:
		print("oops ! you selected the wrong option! sorry!")
elif(a==2):
	print("1. for new user")
	print("2. for existing user")
	ab=int(input("enter here :"))
	if(ab==1):
		armynewuser()
	elif(ab==2):
		armyexistinguser()
	else:
		print("oops ! you selected the wrong option! sorry!")
else:
	print("oops ! you selected the wrong option! sorry!")
	
