n = int(input())
nums = list(map(int,input().split()))
increase = [1 for _ in range(n)]
decrease = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in reversed(range(n)):
    for j in reversed(range(i+1,n)):
        if nums[i] > nums[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[i]

print(max(result))