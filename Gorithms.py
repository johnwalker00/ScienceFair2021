from datetime import datetime, time
import itertools

special_chars = '`~!@#$%^&*()-=_+[]\\{}|;\':",./<>?'
num_chars = '1234567890'
chars = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' + num_chars + special_chars

#Helpful, gets current time in milliseconds
def now_mseconds():
    return datetime.now().hour * 360 * 1000 + datetime.now().minute * 60 * 1000 + datetime.now().second * 1000 + round(datetime.now().microsecond / 1000)

#Got from Stack Overflow
def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(chars, repeat=size):
            yield ''.join(s)

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
        return f'found {password} after {current_guess} loops, {(end_time - start_time) / 1000.0} seconds'
    else:
        #Print defeat message plus time it took
        end_time = now_mseconds()
        return f'could not find {password} after {current_guess} loops, {(end_time - start_time) / 1000.0} seconds'

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
    while not success:
        #Ensure we haven't reached the last word
        if current_guess < len(words):
            #See if we guessed correctly
            if password in [words[current_guess].replace('\n', ''), words[current_guess].replace('\n', '').capitalize()]:
                success = True
                break
            else:
                count += 1
                #Now we try appending numbers
                for i in range(9):
                    if password in [words[current_guess].replace('\n', '') + str(i), words[current_guess].replace('\n', '').capitalize() + str(i)]:
                        success = True
                        break
                    else:
                        count += 1
                        #And special chars
                        for j in range(len(special_chars)):
                            if password in [words[current_guess].replace('\n', '') + str(i) + special_chars[j], words[current_guess].replace('\n', '').capitalize() + str(i) + special_chars[j]]:
                                success = True
                                break
                        if now_mseconds() - start_time >= timeout * 1000:
                            break

                if now_mseconds() - start_time >= timeout * 1000:
                    break
        #Password is not in list
        else:
            current_guess = -1
        current_guess += 1

    if success:
        #Print victory message plus time it took
        end_time = now_mseconds()
        return f'found {password} after {count} loops, {(end_time - start_time) / 1000.0} seconds'
    else:
        #Print defeat message plus time it took
        end_time = now_mseconds()
        return f'could not find {password} after {count} loops, {(end_time - start_time) / 1000.0} seconds'

#Test randomly
def random_test(password: str, timeout: int):
    #Log start time
    start_time = now_mseconds()
    
    success = False
    count = 0
    for guess in iter_all_strings():
        if guess == password:
            success = True
            break
        if now_mseconds() - start_time >= timeout * 1000:
            break
        else:
            count += 1
    if success:
        #Print victory message plus time it took
        end_time = now_mseconds()
        return f'found {password} after {count} loops, {(end_time - start_time) / 1000.0} seconds'
    else:
        #Print defeat message plus time it took
        end_time = now_mseconds()
        return f'could not find {password} after {count} loops, {(end_time - start_time) / 1000.0} seconds'
