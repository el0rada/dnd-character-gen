#dnd stat roll
import random

def statroller():

	stat_list = []

	i=0
	y=0
	stat=0

	while(i<=5):

		roll_list = []
		stat=0

		while(y<=3):
			roll_list.append(random.randint(1,6))
			y+=1

		roll_list.sort()
		roll_list.pop(0)
		
		#print(roll_list)
		
		for x in roll_list:
			stat += x

		stat_list.append(stat)
		i+=1
		y=0

	stat_list.sort()
	#print(stat_list)

	for x in stat_list:
		if(x==3):
			print(str(x)+"  (-4)")
		if(x==4 or x==5):
			print(str(x)+"  (-3)")
		if(x==6 or x==7):
			print(str(x)+"  (-2)")
		if(x==8 or x==9):
			print(str(x)+"  (-1)")
		if(x==10 or x==11):
			print(str(x)+" (+0)")
		if(x==12 or x==13):
			print(str(x)+" (+1)")
		if(x==14 or x==15):
			print(str(x)+" (+2)")
		if(x==16 or x==17):
			print(str(x)+" (+3)")
		if(x==18):
			print(str(x)+" (+1)")

while True:
	statroller()
	x = input("Roll Again (y/N): ")
	if(x==""):
		break
	elif(x=="y"):
		pass
	else:
		break