from datetime import datetime

def test_commons(password: str):
    running = True
    start_time = datetime.now().hour * 360 + datetime.now().minute * 60 + datetime.now().second
    f = open("commonwords.txt", encoding='utf8')
    words = f.readlines()
    f.close()
    
    success = False
    current_guess = 0
    while True:
        if current_guess < len(words):
            if words[current_guess] in [password + '\n', password]:
                success = True
                break
            elif words[current_guess].capitalize() in [password + '\n', password]:
                success = True
                break
        else:
            break
        current_guess += 1
    if success:
        end_time = datetime.now().hour * 360 + datetime.now().minute * 60 + datetime.now().second 
        running = False
        return f'Found {password} after {current_guess} loops, {end_time - start_time} seconds'
    else:
        end_time = datetime.now().hour * 360 + datetime.now().minute * 60 + datetime.now().second 
        running = False
        return f'Could not find {password} after {current_guess} loops, {end_time - start_time} seconds'
