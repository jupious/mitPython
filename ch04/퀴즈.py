
# nums = []
# sum = 0
# for i in range(int(input("입력할 횟수 입력"))):
#     num = int(input(str(i+1)+"번째 숫자 입력"))
#     nums.append(num)
#     sum+=num
# nums.sort()
# count = int(input("몇번씩 점프해서 보여줄까요?"))
# print(str(count)+"번씩 점프해서 보여주면")
# print(nums[::count])
# print("모두 더한값은:",sum)

nums = []

loop = int(input("입력할 횟수 입력"))

num = int(input("1번째 숫자를 입력"))
min = num
max = num
sum = num

for i in range(loop-1):
    num = int(input(str(i+2)+"번째 숫자 입력"))
    sum+=num
    if num < min:
        min = num
    elif num > max:
        max = num
        
nums.sort()
print("입력한 최소값:",min)
print("입력한 최대값:",max)
print("입력한 평균값:",sum/loop)
print("모두 더한값은:",sum)
