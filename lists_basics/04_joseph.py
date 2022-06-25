nums = [number for number in input().split()]
k = int(input())
new_list = []
step = k - 1
index = 0
while True:
    if len(nums) == 0:
        break
    index = (index + step) % len(nums)
    num = nums.pop(index)
    new_list.append(num)
print("[" + ",".join(new_list) + "]")