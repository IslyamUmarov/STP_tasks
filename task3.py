def getNumber(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = int(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return int(getNumber)


a = getNumber("a")
b = getNumber("b")

print("+: {0}, -: {1}, *: {2}, /: {3}".format(a + b, a - b, a * b, a / b))
