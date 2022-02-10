nums = []
sum1 = 0
sum2 = 0
for i in range(1, 1000):
    if i % 2 != 0:
        nums.append(i ** 3)

for index in range(len(nums)):
    num_sum = 0
    j = nums[index]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum1 += nums[index]
    nums[index] += 17
    num_sum = 0
    j = nums[index]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum2 += nums[index]
print(sum1)
print(sum2)