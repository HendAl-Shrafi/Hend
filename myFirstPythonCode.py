nums = []

for i in range(5):
    num = int(input("add number: "))
    nums.append(num)

max = nums[0]
min = nums[0]

for i in nums:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"the max number is {max} \nthe min number is: {min}")

