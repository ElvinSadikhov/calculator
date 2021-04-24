def calculation(line):
    '''
    РАБОТАЕТ КАК КАЛЬКУЛЯТОР ДЛЯ ВСЕХ ОПЕРАЦИЙ СОСТОЯЩИХ ИЗ * / + -
    #####СКОБКИ НЕ УЧИТЫВАЮТСЯ(НЕДОРАБОТАЛ ПОКА)
    '''
    temp=''
    for i in range(len(line)):
        if line[i]=="-" or line[i]=="+" or line[i]=="*" or line[i]=="/":
            temp+=" "+line[i]+" "
        else:
            temp+=line[i]
    new=temp.split()
    if new[1]=="*" or new[1]=="/":
        result=0
    else:
        result=int(new[0])
    '''
    flag=0 это когда самое начал
    flag=1 это когда последняя операция была на умноение или деление
    falg=-1 это когда последняя итерация была сумма или разница
    '''
    flag=0
    for i in range(len(new)):
        if new[i]=="*":
            if flag==1:
                result=result-operation+operation*int(new[i+1])
                operation=operation*int(new[i+1])
            elif flag==-1:
                result-=operation
                if operation>0:
                    operation=int(new[i-1])*int(new[i+1])
                    result+=operation
                else:
                    operation=int(new[i-1])*int(new[i+1])
                    result-=operation
                flag=1
            else:
                operation=int(new[i-1])*int(new[i+1])
                result+=operation
                flag=1           
        if new[i]=="/":
            if flag==1:
                result=result-operation+operation/int(new[i+1])
                operation=operation/int(new[i+1])
            elif flag==-1:
                result-=operation
                if operation>0:
                    operation=int(new[i-1])/int(new[i+1])
                    result+=operation
                else:
                    operation=int(new[i-1])/int(new[i+1])
                    result-=operation
                flag=1
            else:
                operation=int(new[i-1])/int(new[i+1])
                result+=operation
                flag=1
        if new[i]=="-":
            operation=-int(new[i+1])
            result+=operation
            flag=-1
        if new[i]=="+":
            operation=int(new[i+1])
            result+=operation
            flag=-1
    return result
line=input("Type needed camputations:\n")
print("Result is:\n",calculation(line))
