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


a = getNumber("основание")
b = getNumber("степень")

num = a

for i in range(b-1):
    a *= num
print(a)
