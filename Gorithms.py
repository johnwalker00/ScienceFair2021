from datetime import datetime

#Helpful
def now_seconds():
    return datetime.now().hour * 360 + datetime.now().minute * 60 + datetime.now().second

#Looks for a word in commonwords.txt
def test_commons(password: str):
    #Log start time
    start_time = now_seconds()

    #Open file, copy it to a list, and close it
    f = open('commonwords.txt', encoding='utf8')
    words = f.readlines()
    f.close()
    
    #Initialize loop
    success = False
    current_guess = 0
    while True:
        #Ensure we haven't reached the last word
        if current_guess < len(words):
            #See if we got it
            if words[current_guess] in [password + '\n', password]:
                success = True
                break
            #Check if capitalization will fix it
            elif words[current_guess].capitalize() in [password + '\n', password]:
                success = True
                break
        #Password is not in list
        else:
            break
        current_guess += 1
    if success:
        #Print victory message plus time it took
        end_time = now_seconds()
        return f'found {password} after {current_guess} loops, {end_time - start_time} seconds'
    else:
        #Print defeat message plus time it took
        end_time = now_seconds()
        return f'could not find {password} after {current_guess} loops, {end_time - start_time} seconds'

#Looks for a word in dictionary.txt
def test_words(password: str):
    #Log start time
    start_time = now_seconds()

    #Open file, copy it to a list, and close it
    f = open('dictionary.txt')
    words = f.readlines()
    f.close()
    
    #Initialize loop
    success = False
    current_guess = 0
    while True:
        #Ensure we haven't reached the last word
        if current_guess < len(words):
            #See if we guessed correctly
            if words[current_guess] in [password + '\n', password]:
                success = True
                break
            #Check if capitalization will fix it
            elif words[current_guess].capitalize() in [password + '\n', password]:
                success = True
                break
        #Password is not in list
        else:
            break
        current_guess += 1
    if success:
        #Print victory message plus time it took
        end_time = now_seconds()
        return f'found {password} after {current_guess} loops, {end_time - start_time} seconds'
    else:
        #Print defeat message plus time it took
        end_time = now_seconds()
        return f'could not find {password} after {current_guess} loops, {end_time - start_time} seconds'

#Test for dictionary word + numbers
def test_word_num(password: str, digits: int):
    pass

#Test randomly
def random_test(password: str, timeout: int):
    pass
