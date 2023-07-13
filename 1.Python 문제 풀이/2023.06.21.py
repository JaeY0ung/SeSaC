# def opertwoNum():
#     oper = input("연산 모드를 입력하세요(plus / minus / multiply / division): ")
#     a = input("숫자 1을 입력하세요: ")
#     b = input("숫자 2을 입력하세요: ")
#     print("결과: ", end="")
#     if oper =="plus":
#         result = eval(a+'+'+b)
#     elif oper =="minus":
#         result = eval(a+'-'+b)
#     elif oper == "multiply":
#         result = eval(a+'*'+b)
#     elif oper == "division":
#         result = eval(a+'/'+b)
#     else: 
#         result = "잘못 입력하셨습니다"
#     return result

# print(opertwoNum())


# def opertwoNum2():
#     oper = input("연산 모드를 입력하세요(plus / minus / multiply / division): ")
#     a = input("숫자 1을 입력하세요: ")
#     b = input("숫자 2을 입력하세요: ")
#     print("결과: ", end="")
#     oper_dict = {"plus"     : ['+', "덧셈"],
#                  "minus"    : ['-', "뺄셈"],
#                  "multiply" : ['*', "곱셈"],
#                  "division" : ['/', "나눗셈"] }
#     try:
#         print(f"연산: {oper_dict[oper][1]}")
#         result = eval(a + oper_dict[oper][0] + b)
#         return result
#     except ValueError:
#         print("올바른 숫자가 입력되지 않았습니다")
#         print("다시 입력해 주세요")
#         return opertwoNum2()
#     except KeyError:
#         print("올바른 연산이 입력되지 않았습니다")
#         print("다시 입력해 주세요")
#         return opertwoNum2()

# print(opertwoNum2())

# 완벽!!
def oper():
    myoper = input("연산 모드를 입력하세요(plus / minus / multiply / division): ")
    oper_dict = {"plus"     : ['+', "덧셈"],
                 "minus"    : ['-', "뺄셈"],
                 "multiply" : ['*', "곱셈"],
                 "division" : ['/', "나눗셈"] }
    
    if myoper in oper_dict.keys():
        print(f"입력된 연산: {oper_dict[myoper][1]}")
        return oper_dict[myoper][0]
    else:
        print("알 수 없는 연산모드가 입력되었습니다.")
        myoper = oper()

def num1():
    a = input("숫자 1을 입력하세요: ")
    if a.isnumeric() == False:
        print("잘못된 숫자가 입력되었습니다.")
        a = num1()
    return a

def num2():
    b = input("숫자 2을 입력하세요: ")
    if b.isnumeric() == False:
        print("잘못된 숫자가 입력되었습니다.")
        b = num2()
    return b

def mode():
    mode1  = input("종료하시겠습니까? (Y/N): ")
    if mode1 not in ["Y","N"]:
        mode1 = mode()
    return mode1
        
def cal():
    x = num1()
    y = num2()
    operation = oper()
    try:
        result = eval(x + operation + y)
        print(f"결과: {x + operation + y} = {result}")
    except:
        print("연산이 정의되지 않았습니다. 처음부터 다시 입력해주세요.")
        cal()
    mode2 = mode()
    if mode2 == "Y":
        exit(0)
    else:
        cal()

cal()