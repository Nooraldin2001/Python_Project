'''
(Task 1.1) Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
'''
def list_odd_even(x, y):
    odd_list = [num for num in range(x,y) if num %2 != 0]   
    even_list = [num for num in range(x,y) if num %2 == 0]   
    return print('This is the odd list: ',odd_list,'This is the even list: ',even_list)

print(list_odd_even(5,50))         
 

'''
(Task 1.2) Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
'''
def list_Numbers(x, y):
    number_list = [num for num in range(1,101) if num % x == 0 or num % y == 0]   
    return 'This is the numbers that can be divided on x,y: ',number_list

print(list_Numbers(5,10))     
         

