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


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n


a = getNumber("a")
print(factorial(a))
