def fonk(factorial):
    print('туц-туц')
    fonks = 1
    i = 1
    if factorial > 0:
        while i <= factorial:
            fonks *= i
            i += 1
    print(fonks)


fonk(3)
fonk(12)
