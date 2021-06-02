def getNumber(num):
    while type:
        getNumber = input('Введите число ' + num + ': ')
        try:
            getTempNumber = float(getNumber)
        except ValueError:
            print('"' + getNumber + '"' + ' - не является числом')
        else:
            break
    return float(getNumber)


x0 = getNumber("x0")
v0 = getNumber("v0")
t = getNumber("t")
a = g = 9.81

answer = x0 + v0*t - 1/2*a*t*t
print(answer)
