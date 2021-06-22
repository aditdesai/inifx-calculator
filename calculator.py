from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("365x375")
root.iconbitmap("calc.ico")

entry = Text(root, height = 2, width = 25, borderwidth = 4, font = ("Times", 20))
entry.grid(row = 0, column = 0, columnspan = 4)

def action(character):
    entry.insert(INSERT, character)

def clear():
    entry.delete('1.0', 'end')

def isOperand(c):
    return c.isdigit()

def isOperator(c):
    return c in ['^', '/', '*', '+', '-']

def prec(c):
    if(c == '^'):
        return 3
    elif(c == '/' or c == '*'):
        return 2
    elif(c == '+' or c == '-'):
        return 1
    return 0

def result(num1, num2, op):
    if(op == '^'):
        return num1 ** num2
    elif(op == '/'):
        return num1 / num2
    elif(op == '*'):
        return num1 * num2
    elif(op == '+'):
        return num1 + num2
    else:
        return num1 - num2

def evaluate():
    infix = entry.get('1.0', 'end')
    infix = infix[0 : len(infix) - 1]
    operator = []
    operand = []

    ind = -1
    valid = True
    number = ''
    for c in infix:
        ind += 1
        if(c == ' '):
            continue
    
        elif(isOperand(c)):
            number += c
            if(ind == len(infix) - 1):
                operand.append(float(number))
            elif(isOperator(infix[ind + 1]) or infix[ind + 1] == ')'):
                operand.append(float(number))
            else:
                continue

          
        elif(c == '('):
            number = ''
            operator.append(c)
        
        elif(c == ')'):
            number = ''
            while(len(operator) != 0 and operator[-1] != '('):
                num1 = operand.pop()
                num2 = operand.pop()

                if(operator[-1] == '/' and num1 == 0):
                    clear()
                    entry.insert(INSERT, "DIVISION BY 0")
                    return

                operand.append(result(num2, num1, operator.pop()))
            
            operator.pop()
        
        elif(isOperator(c)):
            number = ''
            while(len(operator) != 0 and c != '(' and prec(c) <= prec(operator[-1])):
                num1 = operand.pop()
                num2 = operand.pop()

                if(operator[-1] == '/' and num1 == 0):
                    clear()
                    entry.insert(INSERT, "DIVISION BY 0")
                    return

                operand.append(result(num2, num1, operator.pop()))

            operator.append(c)
        
        else:
            valid = False
            break
        

    if(not valid):
        clear()
        entry.insert(INSERT, "INVALID")
    
    else:
        while(len(operator) != 0):
            num1 = operand.pop()
            num2 = operand.pop()

            if(operator[-1] == '/' and num1 == 0):
                clear()
                entry.insert(INSERT, "DIVISION BY 0")
                return

            operand.append(result(num2, num1, operator.pop()))
        
        clear()
        if(operand[0].is_integer()):
            entry.insert(INSERT, str(int(operand[0])))
        else:
            entry.insert(INSERT, str(operand[0]))


def back():
    entry.delete("end -2 c")

button_clear = Button(root, text = "CLR", width = 5, font = ("Times", 20), bd = 5, command = clear)
button_clear.grid(row = 1, column = 0)

button_back = Button(root, text = "BACK", width = 5, font = ("Times", 20), bd = 5, command = back)
button_back.grid(row = 1, column = 1)

button_equals = Button(root, text = "=", width = 5, font = ("Times", 20), bd = 5, command = evaluate)
button_equals.grid(row = 1, column = 2)

button_exp = Button(root, text = "^", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('^'))
button_exp.grid(row = 1, column = 3)

button1 = Button(root, text = "1", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('1'))
button1.grid(row = 2, column = 0)

button2 = Button(root, text = "2", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('2'))
button2.grid(row = 2, column = 1)

button3 = Button(root, text = "3", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('3'))
button3.grid(row = 2, column = 2)

button_add = Button(root, text = "+", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('+'))
button_add.grid(row = 2, column = 3)

button4 = Button(root, text = "4", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('4'))
button4.grid(row = 3, column = 0)

button5 = Button(root, text = "5", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('5'))
button5.grid(row = 3, column = 1)

button6 = Button(root, text = "6", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('6'))
button6.grid(row = 3, column = 2)

button_minus = Button(root, text = "-", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('-'))
button_minus.grid(row = 3, column = 3)

button7 = Button(root, text = "7", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('7'))
button7.grid(row = 4, column = 0)

button8 = Button(root, text = "8", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('8'))
button8.grid(row = 4, column = 1)

button9 = Button(root, text = "9", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('9'))
button9.grid(row = 4, column = 2)

button_multiply = Button(root, text = "*", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('*'))
button_multiply.grid(row = 4, column = 3)

button_open = Button(root, text = "(", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('('))
button_open.grid(row = 5, column = 0)

button0 = Button(root, text = "0", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('0'))
button0.grid(row = 5, column = 1)

button_close = Button(root, text = ")", width = 5, font = ("Times", 20), bd = 5, command = lambda : action(')'))
button_close.grid(row = 5, column = 2)

button_divide = Button(root, text = "/", width = 5, font = ("Times", 20), bd = 5, command = lambda : action('/'))
button_divide.grid(row = 5, column = 3)



root.mainloop()