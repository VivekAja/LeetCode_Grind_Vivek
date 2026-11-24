class Solution:
    def lcm(a, b):
        res = max(a, b)
        while res % a != 0 or res % b != 0:
            res += max(a, b)
        return res
    def gcd(c, d):
        if c ==0:
            return d
        return gcd(d%c, c)
    def maxLength(self, nums: List[int]) -> int:
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i:j+1]
                res = temp[0]
                result = 1
                if len(temp) == 1:
                    cur_gcd = temp[0]
                    cur_lcm = temp[0]
                else:
                    for k in range(1, len(temp)):
                        res = lcm(res, temp[k])
                    cur_lcm = res
                    gcdres = temp[0]
                    for l in range(1, len(temp)):
                        gcdres = gcd(temp[l], gcdres)
                    cur_gcd = gcdres
                for c in temp:
                    result *= c
                if result == cur_gcd * cur_lcm:
                    ret.append(len(temp))
                #print(ret, result, cur_gcd)
        return max(ret)