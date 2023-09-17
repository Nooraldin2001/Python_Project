class Tasks_level_1():
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

task1 = Tasks_level_1()
print(task1.Howmany_Words("Create", "Create a function Create that takes a sentence Create and word and remove the Create word from the sentence"))
#print(task1.Remove_Words("Create", "Create a function that takes a sentence and word and remove the word from the sentence"))
#print(task1.list_Numbers(5,10))     
#print(task1.list_Mul(1,10))
#print(task1.remove_duplicated_words('Create Create a a function function that that takes takes a a a sentence sentence and and prints the sentence without duplicated duplicated duplicated words'))
#print(task1.list_odd_even(5,50))         
#print(task1.Count_Words('Create a function that takes a sentence and prints how many words in the sentence do not count the spaces'))
