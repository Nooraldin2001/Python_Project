class Tasks_level_1():

    '''                             Python Task Level 1:                                  '''

    '''
    (Task 1.1) Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
    the x,y range
    '''
    def list_odd_even(self, x, y):
        odd_list = [num for num in range(x,y) if num %2 != 0]   
        even_list = [num for num in range(x,y) if num %2 == 0]   
        return print('This is the odd list: ',odd_list,'This is the even list: ',even_list)    

    '''
    (Task 1.2) Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
    be divided on x,y
    '''
    def list_Numbers(self,x, y):
        number_list = [num for num in range(1,101) if num % x == 0 or num % y == 0]   
        return 'This is the numbers that can be divided on x,y: ',number_list



    '''
    (Task 1.3) Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
    '''
    def list_Mul(self,a, b):
        # number_list = [x * y for x in range(1,y+1)]   
        # return 'This is the multiplication table from x to y: ',number_list
        for i in range(a, b+1):
            print("multiplication table for", i)
            for j in range(1,11):
                print(i, "*", j, "=", i * j)


    '''
    (Task 1.4) Create a function that takes a sentence and prints the sentence without duplicated words
    '''
    def remove_duplicated_words(self,listwords):
        listwords = listwords.split(' ')
        return set(listwords)  

    '''
    (Task 1.5)Create a function that takes a sentence and prints how many words in the sentence do not count the
    spaces
    '''
    def Count_Words(self,listwords):
        listwords = listwords.split()
        number_of_words = len(listwords)
        return number_of_words
    
    '''
    (Task 1.6)Create a function that takes a sentence and word and remove the word from the sentence
    '''
    def Remove_Words(self,removed,listwords):
        listwords = listwords.split()
        new_listwords = [word for word in listwords if word != removed]
        new_listwords = " ".join(new_listwords)

        return new_listwords
    
    '''
    (Task 1.6)Create a function takes a sentence and a word and prints how many time the word used in the sentence
    '''
    def Howmany_Words(self,reapeted,listwords):
        listwords = listwords.split()
        reapetedwords = [word for word in listwords if word == reapeted]
        number_of_reaptead_words = len(reapetedwords)
        return number_of_reaptead_words
    
    '''
    (Task 1.8) Create a function that takes x,y and prints all the number that can be divide by y from x to 100
    '''
    def By_Y_From_X(self,x,y):
        number_list = [num for num in range(x,101) if num % y == 0]   
        return 'This is the numbers that can be divided on x,y: ',number_list



#task1 = Tasks_level_1()                  #You can just remove the comment and run the code 
#print(task1.By_Y_From_X(80,3))
#print(task1.Howmany_Words("Create", "Create a function Create that takes a sentence Create and word and remove the Create word from the sentence"))
#print(task1.Remove_Words("Create", "Create a function that takes a sentence and word and remove the word from the sentence"))
#print(task1.list_Numbers(5,10))     
#print(task1.list_Mul(1,10))
#print(task1.remove_duplicated_words('Create Create a a function function that that takes takes a a a sentence sentence and and prints the sentence without duplicated duplicated duplicated words'))
#print(task1.list_odd_even(5,50))         
#print(task1.Count_Words('Create a function that takes a sentence and prints how many words in the sentence do not count the spaces'))




class Tasks_level_2():

    '''                                  Python Task Level 2 :                                  '''

    '''
    (Task 2.1)Transform all names to uppercase using [normal list - list comprehension - functional programming]
    '''
    def Tranform_To_Upper(self, names):
        #names = names.split()
        Uppernames = [name.upper() for name in names ]
        #Uppernames = Uppernames.join(" ")
        return Uppernames
    
    '''
    (Task 2.2) Get the names that contains (a) in a list using [normal list - list comprehension - functional programming]
    '''
    def Words_Contains_A(self, names):
        #names = names.split()
        namesContains_A = [name for name in names if 'a' in name]
        #Uppernames = Uppernames.join(" ")
        return namesContains_A
    
    '''
    (Task 2.3) Get the names that starts with (t) in a list using [normal list - list comprehension - functional programming]
    '''
    def Word_Start_With_T(self, names):
        #names = names.split()
        namesStart_With_T = [name for name in names if name.startswith('t')]
        #Uppernames = Uppernames.join(" ")
        return namesStart_With_T
    
    '''
    (Task 2.4) Get the names that contains 2 or more (a) letter using [normal list - list comprehension - functional programming]
    '''
    def Word_Contains_2A(self, names):
        #names = names.split()
        namesContains_2A = [name for name in names if name.count('a') >= 2]
        #Uppernames = Uppernames.join(" ")
        return namesContains_2A
    
    '''
    (Task 2.5) Print a list contains the len of each word in the list using [normal list - list comprehension - functional programming]
    '''
    def Words_Lenght(self, names):
        #names = names.split()
        nameslenght = [len(name) for name in names ]
        #Uppernames = Uppernames.join(" ")
        return nameslenght
    
    '''
    6. Unpack the list in
    7. a,b , a= the first index , b = rest of the list
    '''
    def slicing_7(self, list):
        a = list[:1]
        b = list[1:]
        return a,b

    '''
    8. a = the first index , b = the last index
    '''
    def slicing_8(self, list):
        a = list[:1]
        lastindex = len(list)-1
        b = [list[lastindex]]
        return a,b
    '''
    9. a = the first index , b = the second index
    '''
    def slicing_9(self, list):
        a = [list[0]]
        b = [list[1]]
        return a,b


#task2 = Tasks_level_2()                  #You can just remove the comment and run the code 
#Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#print(task2.slicing_9(Names))
#print(task2.slicing_8(Names))
#print(task2.slicing_7(Names))
#print(task2.Words_Lenght(Names))
#print(task2.Word_Contains_2A(Names))
#print(task2.Word_Start_With_T(Names))
#print(task2.Tranform_To_Upper(Names))
#print(task2.Words_Contains_A(Names))

from datetime import datetime, timedelta
import re

class Task_level_3():
        '''                             Python Task Level 1:                                  '''

        """
            (Task 3.1)Build a countdown calculator. Write some code that can take two dates as input, and then calculate the amount of time between them
        """
        def dates_countdown(self, startdate, enddate):

            datelist = []


            dates = startdate
            while dates <= enddate:
                datelist.append(dates)
                dates += timedelta(days=1)
            
            calculatedDates = [date.strftime("%Y-%m-%d") for date in datelist]
            return calculatedDates
        

        '''
            (Task 3.1)Make a temperature/measurement converter. Write a script that can convert Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different ways
        '''
        def measures(self, number, mesure):

            if mesure == "Celcius To Fahrenheit":
                number = (number - 32)*5/9

            elif mesure == "Fahrenheit To Celcius":
                number = (number * 9/5)+32
            
            elif mesure == "Inches To Centimeters":
                number = number * 2.54
            
            elif mesure == "Centimeters To Inches":
                number = number / 2.54

            elif mesure == "Pounds To Kilograms":
                number = number * 0.453592
            
            elif mesure == "Pounds To Kilograms":
                number = number / 0.453592


            return print(mesure , '=', number)
        
        '''
        (Task 3.2)Build an email slicer : create a function that takes an email as input and retrieve the username and domain of the email

        '''
        def email_slicer(self, email):
            pattern = '@'
            split_email = re.split(pattern,email)
            username = split_email[0]
            domain = split_email[1]
            return print('your domain and username is ', username, domain)
        
        '''
        (Task 3.3)Currency converter : create a python script that takes a money with currency sign and convert it to some other currencies , the code should be like the game we did before
        '''
class Currency_converter:
    def __init__(self):
        self.converted_money = None
        while True:
            print('''Welcome to Noor Exchange. Please press Enter to start exchange:
                 1: From EGP to USD
                 2: From EGP to Euro
                 3: From EGP to Dirhams''')
            
            convert_mode = int(input("Please insert the mode number: "))
            money = int(input("Please insert the money: "))

            if convert_mode == 1:
                self.converted_money = money * 30
                print('Your money will be after changing to USD:', self.converted_money)
            elif convert_mode == 2:
                self.converted_money = money * 40
                print('Your money will be after changing to Euro:', self.converted_money)
            elif convert_mode == 3:
                self.converted_money = money * 10
                print('Your money will be after changing to Dirhams:', self.converted_money)
            else:
                print('Exit')
                break

            exchange_again = input('press any key to change another currancy or press x to exit ')
            if exchange_again == 'x': 
                print('thank you for using noor exchange')





# Create an instance of the Currency_converter class
converter = Currency_converter()

        #def Currency_converter(self, from_currency, to_currency):

        






task_3 = Task_level_3()

#email = input("Enter your email please ")
#task_3.email_slicer(email)
#mesures = input("Enter your mesure please ")
#numbers = int(input("Enter the number you wnat to convert "))
#print(task_3.measures(numbers, mesures))

#start = input("Enter a start date (YYYY-MM-DD)")
#end = input("Enter a end date (YYYY-MM-DD)")
#print(task_3.dates_countdown(datetime.strptime(start, "%Y-%m-%d"),datetime.strptime(end, "%Y-%m-%d")))





    