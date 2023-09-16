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
         

'''
(Task 1.3) Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
'''
def list_Mul(a, b):
    # number_list = [x * y for x in range(1,y+1)]   
    # return 'This is the multiplication table from x to y: ',number_list
    for i in range(a, b+1):
        print("multiplication table for", i)
        for j in range(1,11):
            print(i, "*", j, "=", i * j)

print(list_Mul(1,10))

'''
(Task 1.4) Create a function that takes a sentence and prints the sentence without duplicated words
'''
def remove_duplicated_words(listwords):
    listwords = listwords.split(' ')
    return set(listwords)  


        


print(remove_duplicated_words('Create Create a a function function that that takes takes a a a sentence sentence and and prints the sentence without duplicated duplicated duplicated words'))