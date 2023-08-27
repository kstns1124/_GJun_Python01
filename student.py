import random

def __getAllNames(fileName:str="names.txt")->list[str]:
    '''
    get txt-file  contents
    '''
    names: list[str] = []
    with open("names.txt", mode = "r", encoding="utf-8") as Namefile:    
        for line in Namefile:
            names.append(line.rstrip("\n"))
    return names

def __getRandName(num:int = 1)->list[str]:
    '''
    get random name from txt-file  contents
    '''
    names = __getAllNames()
    #choices = [random.choice(names) for _ in range(num)]
    choices = random.choices(names, k = num )
    return choices

def get_students(num:int = 1)->list[list]:
    '''
    get name and ints from txt-file  contents
    '''
    names = __getAllNames()
    StudentScore:list[list] = []
    for i in range(0, num):
        StudentScore.append([names[i]] + [random.randint(0, 100) for _ in range(0, 5)]);
    return StudentScore