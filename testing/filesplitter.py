import os

lines_per_file = 5000
smallfile = None
with open('testing/testpasswords.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            dirname = 'testing/testing'+str(int(lineno/lines_per_file)+1)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            small_filename = dirname + '/testpasswords5k.txt'
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()