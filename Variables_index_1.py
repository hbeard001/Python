nums=[100,3,75,101]
i=1
big=nums[0]
while i<len(nums):
    if nums[i]>big:
        big=nums[i]
    i=i+1
print("Highest number is:",big)
