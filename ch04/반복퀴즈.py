sum = 0
for i in range(101):
    sum += i
print(sum)

print("==============================")

sum = 0
for i in range(1, 100, 2):
    sum+=i
print(sum)

print("==============================")

sum = 0
for i in range(50, 100, 2):
    sum+=i
print(sum)

print("==============================")

for i in range(2,10,1):
    print(i,"단 ============")
    for j in range(2, 10, 1):
        print(i,"*",j,"=",i*j)