import tkinter as tk

'''
GUI 
'''
window = tk.Tk()  # initialised window and title
window.title('BinaryDecimalHex Converter v1 by Daniel',)

window.resizable(False, False)

canvas = tk.Canvas(window, width=400, height=300, bg='palegreen4')  # window size
canvas.pack()

label = tk.Label(window, text='BinaryDecimalHexConverter', bg='palegreen1')  # window label
label.config(font=('helvetica', 14))
canvas.create_window(200, 25, window=label)

canvas.create_line(180, 150, 220, 150, arrow=tk.LAST)

convert = [  # option lists
    'Decimal',
    'Hexadecimal',
    'Binary'
    ]

inputVariable = tk.StringVar(window)
inputVariable.set(convert[0])

outputVariable = tk.StringVar(window)
outputVariable.set(convert[0])

inputOpt = tk.OptionMenu(window, inputVariable, *convert)
inputOpt.config(width=10, font=('Helvetica', 10), bg='palegreen1')
inputOpt.place(x=33, y=60)

outputOpt = tk.OptionMenu(window, outputVariable, *convert)
outputOpt.config(width=10, font=('Helvetica', 10), bg='palegreen1')
outputOpt.place(x=253, y=60)


entryInput = tk.Entry(window)  # user input
entryInput.place(x=30, y=140)

entryOutput = tk.Entry(window)
entryOutput.place(x=250, y=140)

'''
CONVERT HANDLING
'''


def checkValidChar(inputType, num):
    global entryOutput
    validChar = []
    if inputType == 'Decimal':
        validChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif inputType == 'Binary':
        validChar = ['0', '1']
    elif inputType == 'Hexadecimal':
        validChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for char in num:
        if char not in validChar:
            num = 'Invalid character'
            v = tk.StringVar(window, value=num)
            entryOutput = tk.Entry(window, textvariable=v)
            entryOutput.place(x=250, y=140)
            return False


def binToDec(binary):
    powerOfTwo = 0
    total = 0

    for j in binary[::-1]:  # flips number to iterate right left
        if int(j) == 1:
            total += 2 ** powerOfTwo
        powerOfTwo += 1
    return total


binString = ''


def decToBin(num):
    global binString
    if num == 0:
        return 0
    if int(num) > 0:
        rem = int(num) % 2
        binString += str(rem)
        decToBin(num / 2)
    return binString[::-1]


hexString = ''
hexNums = {10: 'A',
           11: 'B',
           12: 'C',
           13: 'D',
           14: 'E',
           15: 'F'}


def decToHex(num):
    global hexString
    if num == 0:
        return 0
    if int(num) > 0:
        rem = int(num) % 16
        if rem >= 10:
            rem = hexNums[rem]
        hexString += str(rem)
        decToHex(num / 16)
    return hexString[::-1]


def hexToDec(num):
    total = 0
    power = 0
    reverseHexNums = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    for k in num[::-1]:
        try:
            total += int(k) * (16 ** power)
        except ValueError:
            total += reverseHexNums[k] * (16 ** power)
        power += 1
    return total


def hexToBin(num):
    return decToBin(hexToDec(num))


def binToHex(num):
    return decToHex(binToDec(num))


'''
ON BUTTON PRESS (ENTER)
'''


def printOutput():  # activates on button press, prints convert to second box
    global entryOutput
    global binString
    global hexString
    num = entryInput.get()  # handles all mirror cases at default state
    if checkValidChar(inputVariable.get(), num) is False:  # handles all invalid inputs for the num bases
        return 0

    if inputVariable.get() == 'Decimal' and outputVariable.get() == 'Hexadecimal':
        num = decToHex(int(num))
    elif inputVariable.get() == 'Decimal' and outputVariable.get() == 'Binary':
        num = decToBin(int(num))
    elif inputVariable.get() == 'Binary' and outputVariable.get() == 'Hexadecimal':
        num = binToHex(num)
    elif inputVariable.get() == 'Binary' and outputVariable.get() == 'Decimal':
        num = binToDec(num)
    elif inputVariable.get() == 'Hexadecimal' and outputVariable.get() == 'Binary':
        num = hexToBin(num)
    elif inputVariable.get() == 'Hexadecimal' and outputVariable.get() == 'Decimal':
        num = hexToDec(num)
    hexString = ''
    binString = ''
    v = tk.StringVar(window, value=num)
    entryOutput = tk.Entry(window, textvariable=v)
    entryOutput.place(x=250, y=140)


button = tk.Button(window, text="Enter", bg='palegreen1', command=printOutput)
button.place(x=180, y=200)


'''
MAIN LOOP
'''

window.mainloop()
