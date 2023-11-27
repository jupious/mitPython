'''numbers = []
numbers.append(input("첫 번째 숫자 입력 :"))
numbers.append(input("두 번째 숫자 입력 :"))
numbers.append(input("세 번째 숫자 입력 :"))
numbers.append(input("네 번째 숫자 입력 :"))
numbers.append(input("다섯 번째 숫자 입력 :"))

print(numbers[int(input("몇번째 숫자를 보여줄까?"))-1])

n = input("첫 번째 숫자 입력 :")+input("두 번째 숫자 입력 :")+input("세 번째 숫자 입력 :")+input("네 번째 숫자 입력 :")+input("다섯 번째 숫자 입력 :")
print(n[int(input("몇 번째 숫자를 보여줄까?"))-1])

number1 = [input("첫 번째 숫자 입력 :"),input("두 번째 숫자 입력 :"),input("세 번째 숫자 입력 :"),input("네 번째 숫자 입력 :"),input("다섯 번째 숫자 입력 :")]
print(number1[int(input("몇번째? :"))-1])'''

################################################################
'''
n1 = input("첫 번째 숫자 입력 :")
n2 = input("두 번째 숫자 입력 :")
n3 = input("세 번째 숫자 입력 :")
n4 = input("네 번째 숫자 입력 :")
n5 = input("다섯 번째 숫자 입력 :")
numbers1 = [n1, n2, n3, n4, n5]
spoint = input("어디부터?")
epoint = input("어디까지?")
print(numbers1[int(spoint)-1:int(epoint)])
numbers1.sort()
print(numbers1)
numbers2 = [n5, n4, n3, n2, n1]
print(numbers2)
'''


'''
n1 = input("첫 번째 숫자 입력 :")
n2 = input("두 번째 숫자 입력 :")
n3 = input("세 번째 숫자 입력 :")
n4 = input("네 번째 숫자 입력 :")
n5 = input("다섯 번째 숫자 입력 :")
numbers3 = []
numbers4 = []
numbers3.append(n1)
numbers3.append(n2)
numbers3.append(n3)
numbers3.append(n4)
numbers3.append(n5)

numbers4.append(n1)
numbers4.append(n2)
numbers4.append(n3)
numbers4.append(n4)
numbers4.append(n5)
spoint = input("어디부터?")
epoint = input("어디까지?")
print(numbers3[int(spoint)-1:int(epoint)])
numbers3.sort()
print(numbers3)

print(numbers4[::-1])
'''
'''
n1 = input("첫 번째 숫자 입력 :")
n2 = input("두 번째 숫자 입력 :")
n3 = input("세 번째 숫자 입력 :")
n4 = input("네 번째 숫자 입력 :")
n5 = input("다섯 번째 숫자 입력 :")
numbers5 = []
numbers5.append(int(n1))
numbers5.append(int(n2))
numbers5.append(int(n3))
numbers5.append(int(n4))
numbers5.append(int(n5))

spoint = input("어디부터?")
epoint = input("어디까지?")
print(numbers5[int(spoint)-1:int(epoint)])
numbers6 = numbers5[::-1]
numbers5.sort()
print(numbers5)
print(numbers6)'''

