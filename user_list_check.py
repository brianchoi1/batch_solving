# file = open("user_list_AC.txt", "w")
# file.write("blabla is nothing.")
# file.close();
# id = 'jaeyoung.choi'
id = 'yoonj.lee'
def check_string():
    with open('user_list_AC.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if id in line:
            return True # The string is found
    return False  # The string does not exist in the file

if check_string():
    print('True')
else:
    print('False')