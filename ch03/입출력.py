'''num1 = int(input("첫 번째 정수를 입력: "))
num2 = int(input("두 번째 정수를 입력: "))

print("몫은",num1//num2)
print("입력한 숫자는",str(num1)+"-"+str(num2))'''


colors = ['red', 'blue', 'green']
print(len(colors))
test = 'aaa'
print(len(test))
'''test2 = 1000
print(len(test2))'''
color2 = ['aa', 'bb']
colors.append(color2)
print(colors)
colors[3].append('cc')
print(colors)

t = [1,2,3]
a, b, c = t
print(t,a,b,c)

a = 100
b = '200'
print(a is not int(b))

a = [1]
b = ['a','b','c']
b[1] = a[0:1]
print(b)

fruits = ['a','b','c','g','o','s','m']
print(fruits[-3:], fruits[1::3])

# fruits.remove(fruits)
# print(fruits)

first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)
print(type(fruits.sort()))