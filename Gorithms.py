from datetime import datetime

#Helpful, gets current time in milliseconds
def now_mseconds():
    return datetime.now().hour * 360 * 1000 + datetime.now().minute * 60 * 1000 + datetime.now().second * 1000 + round(datetime.now().microsecond / 1000)

#Looks for a word in a file
def test_file(password: str, input_file: str):
    #Log start time
    start_time = now_mseconds()

    #Open file, copy it to a list, and close it
    f = open(input_file, encoding='utf8')
    words = f.readlines()
    f.close()
    
    #Initialize loop
    success = False
    current_guess = 0
    while True:
        #Ensure we haven't reached the last word
        if current_guess < len(words):
            #See if we guessed correctly
            if words[current_guess].replace('\n', '') == password:
                success = True
                break
            #Check if capitalization will make our guess correct
            elif words[current_guess].replace('\n', '').capitalize() == password:
                success = True
                break
        #Password is not in list
        else:
            break
        current_guess += 1
    if success:
        #Print victory message plus time it took
        end_time = now_mseconds()
        return f'found {password} after {current_guess} loops, {end_time - start_time} milliseconds'
    else:
        #Print defeat message plus time it took
        end_time = now_mseconds()
        return f'could not find {password} after {current_guess} loops, {end_time - start_time} milliseconds'

#Test for dictionary word + numbers
def test_word_num(password: str, input_file: str, timeout: int):
    #Log start time
    start_time = now_mseconds()

    #Open file, copy it to a list, and close it
    f = open(input_file, encoding='utf8')
    words = f.readlines()
    f.close()
    
    #Initialize loop
    success = False
    current_guess = 0
    count = 0
    while True:
        #Ensure we haven't reached the last word
        if current_guess < len(words):
            #See if we guessed correctly
            if words[current_guess].replace('\n', '') == password:
                success = True
                break
            #Check if capitalization will make our guess correct
            elif words[current_guess].replace('\n', '').capitalize() == password:
                success = True
                break
            else:
                #Now we try appending numbers
                for i in range(9):
                    if words[current_guess].replace('\n', '') + str(i) == password:
                        success = True
                        break
                    elif words[current_guess].replace('\n', '').capitalize() + str(i) == password:
                        success = True
                        break
                    else:
                        count += 1
        #Password is not in list
        else:
            break
        current_guess += 1
        if now_mseconds() - start_time >= timeout * 1000:
            break

    if success:
        #Print victory message plus time it took
        end_time = now_mseconds()
        return f'found {password} after {count} loops, {end_time - start_time} milliseconds'
    else:
        #Print defeat message plus time it took
        end_time = now_mseconds()
        return f'could not find {password} after {count} loops, {end_time - start_time} milliseconds'



#Test randomly
def random_test(password: str, timeout: int):
    pass
