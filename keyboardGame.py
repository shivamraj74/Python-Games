import msvcrt 
import time 

high_score = 20.00
name = "Shivam Raj"
while 1: 
	distance = int(0) 
	print('\n--------------------------------------------------------------') 
	print('\n\nWelcome to the 100m sprint, tap w and e rapidly to move! ') 
	print('* = 10m') 
	print('\nCurrent record : ' + str(high_score) + ' by: ' + name) 
	print('\nPress enter to start! ') 
	input() 
	print('Ready...') 
	time.sleep(1) 
	print("Let's GO!") 

	start_time = time.time() 
	while distance < 10: 

		k1 = msvcrt.getch().decode('ASCII') 
		if k1 == 'w': 
			k2 = msvcrt.getch().decode('ASCII') 
			if k2 == 'e': 
				distance += 1
				if distance == 5: 
					print("* You've covered the half distance!") 
				elif distance % 1 == 0: 
					print('*') 

	fin_time = time.time() - start_time 
	fin_time = round(fin_time, 2) 

	print('Well done, Congratulations on successfully completing the race! ') 
	print('You took', fin_time, 'seconds to reach the finish line') 

	if fin_time < high_score: 
		print("Well done you've achieved a new high score! ") 
		name = input("Can you please write your name : ") 
		high_score = fin_time 
