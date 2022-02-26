import calendar

print(('leap year validator'.upper()))
print('(validates year using Gregorian calender)'.title())

user_query = input('\nwhat year do you seek answers  :  ')

year = int(user_query)
test1,test2 = year%4, year%100

left_hand_exp_result =  0
right_hand_exp_result = 0

x= test1==left_hand_exp_result
y= test2==right_hand_exp_result

if x == True and y== False:
	print('\n'*2+'it\'s a Leap Year')
else:
	print('\n'*2+'Not a Leap Year')

print('\n'*2,calendar.month(year,2))
