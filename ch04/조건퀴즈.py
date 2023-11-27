# if int(input("숫자 입력 :")) % 2 == 0:
#     print("짝수다.")
# else:
#     print("홀수다.")
num = int(input("숫자 입력 :"))
if  num % 2 == 0:
    if num > 100:
        print("100보다 큰짝수다.")
    elif num == 100:
        print("100이다")
    else:
        print("100보다 작은 짝수다. ")
else:
    print("홀수다.")