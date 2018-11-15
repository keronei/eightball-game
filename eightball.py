import sys
from random import randrange
from time import sleep

def predictor():
    answers_array = []
    
    with open('answers.config') as config_content:
        
        count_answers = 0
    
        for each_answer in config_content:
            answers_array.append(each_answer)
            count_answers += 1
    
    choosen_random_answer_idx = randrange(count_answers)#randrange is O(1) which is suitable for algo
            
    choosen_answer = answers_array[choosen_random_answer_idx]
    
    
    return choosen_answer

def answers_count():
    answers_array = []
    
    count_answers = 0
    
    with open('answers.config') as config_content:
                 
        for each_answer in config_content:
            answers_array.append(each_answer)
            count_answers += 1
    
    return count_answers

def check_python_version():
    
    #parse the response to see if OK
    
    if sys.version_info < (3,0):
        sys.stdout.write ('\nPlease run with version 3 or higher\n (Or use python3 script.py)\n')
        
        sys.exit('Bye!')
    else:
        return
    
def show_response(user_question):
    while True:
                
        if user_question in {'quit','q','no','e','exit'}:
            sys.exit('Bye! Exiting...')
        else:
            print ('Thinking wisely :')
            for i in range(21):
                sys.stdout.write('\r')
                sys.stdout.write("[%-20s]%d%%" % ('='*i,5*i))
                sys.stdout.flush()
                sleep(0.25)
            print('\n')               
            selected_answer = predictor()
            print(selected_answer)
            user_question = input('Got another question? Go ahead: \n')
            
    
def main():

    check_python_version()
    user_response = input('Welcome! Ask for an advice. \n To exit, reply with \'e\': \n')
    show_response(user_response)
    
              
if __name__ == '__main__':
    main()