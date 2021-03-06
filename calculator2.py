"""
Будем решать с помощью обратной Польской нотации
"""
def upgradeLine(line):
    """Убирает все пробелы и добавляет в LIST все числа(операнды) и знаки(операции)
    """
    lst=[]
    number=""
    for letter in line:
        if letter==" ":
            continue
        if letter not in ["+","-","*","/","(",")"]:
            number+=letter
        else:
            if number!="":
                lst+=[int(number)]+[letter]
            else:
                lst+=[letter]
            number=""
    #print(number)
    if number!="":
        lst+=[int(number)]
    return lst

def stack(lst):
    massiv_vixoda=[]###
    stack=[]
    for NumOp in lst:
        if type(NumOp)==int:
            massiv_vixoda.append(NumOp)
        else:	#если это операция а не число
            if NumOp=="(":
                stack.append(NumOp)
            elif NumOp==")":
                index=stack.index("(")
                while len(stack)>0 and stack[-1]!="(":
                    massiv_vixoda+=stack[-1]
                    stack.pop(-1)
                stack.pop()
            elif len(stack)==0:
                stack.append(NumOp)
            elif Prioritet(stack[-1])> Prioritet(NumOp):
                flag=0
                for i in range(len(stack)-1,-1,-1):
                    if Prioritet(stack[i])>Prioritet(NumOp) and flag==0:
                        massiv_vixoda+=stack.pop(i)
                    else:
                        flag=1
                stack.append(NumOp)
            elif Prioritet(stack[-1])== Prioritet(NumOp):
                flag=0
                for i in range(len(stack)-1,-1,-1):
                    if Prioritet(stack[i])==Prioritet(NumOp) and flag==0:
                        massiv_vixoda+=stack.pop(i)
                    else:
                        flag=1
                stack.append(NumOp)
            elif Prioritet(stack[-1])<Prioritet(NumOp):
                stack.append(NumOp)
            else:###
                stack.append(NumOp)
    for i in range(len(stack)-1,-1,-1):
        massiv_vixoda+=stack[i]
    return massiv_vixoda

def Prioritet(operation):
    if operation in ["*","/"]:
        return 2
    if operation in ["+","-"]:
        return 1
    else:
        return 0
    
def calculation(lst):
    newlst=[]
    for NumOp in lst:
        if type(NumOp)==int:
            newlst.append(NumOp)
        else:
            num2=newlst.pop()
            num1=newlst.pop()
            if NumOp=="+":
                newlst.append(num1+num2)
            if NumOp=="-":
                newlst.append(num1-num2)
            if NumOp=="*":
                newlst.append(num1*num2)
            if NumOp=="/":
                if num2==0:
                    print("DIVISON BY ZERO!")
                    return
                else:
                    newlst.append(num1/num2)
    return newlst[0]

line=input("Type your calculation:")
if not calculation(stack(upgradeLine(line))) is None:
    print(calculation(stack(upgradeLine(line))))
