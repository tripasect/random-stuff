def integerQ(s):
    try:
        int(s)
        if int(s) == float(s):
            return True
    except ValueError:
        return False

def printDic(dic):
    for i in range(1, len(dic) + 1):
        print(f"{i}. {dic[i]}")
    while True:
        path = input('> ')
        if integerQ(path):
            return int(path)
        else:
            pass
