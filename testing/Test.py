from Gorithms import *

def has_num(string: str):
    return any(s.isnumeric() for s in string)

def has_sp_char(string: str):
    return any(not s.isalnum() for s in string)

def has_cap(string: str):
    return any(s.isupper() for s in string)

def has_low(string: str):
    return any(s.islower() for s in string)

def write_result(password, alg_common_pwd, alg_common_pwd_time, alg_dictionary, alg_dictionary_time, alg_dictionary_num, alg_dictionary_num_time, alg_random, alg_random_time, length, numbers, special, capitals, lowercase) :
    with open('testing/out.csv', 'a') as csv_file:
        csv_file.write(password + ',' + alg_common_pwd + ',' + alg_common_pwd_time + ',' + alg_dictionary + ',' + alg_dictionary_time + ',' + alg_dictionary_num + ',' + alg_dictionary_num_time + ',' + alg_random + ',' + alg_random_time + ',' + str(length) + ',' + str(numbers) + ',' + str(special) + ',' + str(capitals) + ',' + str(lowercase))
        
        csv_file.write('\n')

def call_algs(password: str, timeout: int):
    common_result = test_file(password, 'data/commonwords.txt')
    dict_result = test_file(password, 'data/dictionary.txt')
    dict_num_result = test_word_num(password, 'data/dictionary.txt', timeout)
    random_result = random_test(password, timeout) 

    write_result(password, common_result[0], common_result[1], dict_result[0], dict_result[1], dict_num_result[0], dict_num_result[1], random_result[0], random_result[1], len(password), has_num(password), has_sp_char(password), has_cap(password), has_low(password))

with open('testing/testpasswords.txt') as password_file:
    for i in range(100):
        word = password_file.readline().replace('\n', '')
        call_algs(word, 10)
        print(str(i) + ' ' + word)