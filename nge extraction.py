def solution(arr):
    nums = []
    out = ""
    for i in arr:
        if len(nums) > 0:
            if i == nums[-1] + 1:
                nums.append(i)
            else:
                if len(nums) > 2:
                    out += str(nums[0])+'-'+str(nums[-1])+','
                if len(nums) == 2:
                    for r in nums:
                        out += str(r) + ','
                elif len(nums) == 1:
                    out += str(nums[0]) +','
                nums = [i]
        else:
            nums.append(i)
    if len(nums) > 0:
        if i == nums[-1] + 1:
            nums.append(i)
        else:
            if len(nums) > 2:
                out += str(nums[0]) + '-' + str(nums[-1]) + ','
            if len(nums) == 2:
                for r in nums:
                    out += str(r) + ','
            elif len(nums) == 1:
                out += str(nums[0]) + ','
            nums = [i]
    return out[:-1]


print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))