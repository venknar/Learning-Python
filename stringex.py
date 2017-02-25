def findCount(a, b):
    strLen = len(b)
    count = 0
    while (True):
        pos = b.index(a)
        if (pos != -1):
            count += 1
        if (pos+1 >= strLen):
            break;
        b = b[:pos+1]
       
    return count

res = findCount("hey", "hey mike did you eat whey or they lied")
print(res)