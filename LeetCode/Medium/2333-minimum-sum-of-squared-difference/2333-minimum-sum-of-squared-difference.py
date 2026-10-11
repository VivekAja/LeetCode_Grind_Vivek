class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        for i,j in zip(nums1, nums2):
            diff.append(abs(i - j)) #getting the difference between two series

        k = k1+k2 #Doesn't matter coz those are the number of changes and changes have to bring the square no. to a min

        if sum(diff) <= k:  #if the diff values can be set to 0 then return 0
            return 0

        diff.sort(reverse = True) #Sort the diff list to focus on reducing the max values to a lower value
        diff.append(0) #Required to start comparing the two values

        for i in range(len(diff)-1):
            count = i+1
            gap = diff[i] - diff[i+1] # if diff = [10, 8, 3] then we need to bring it to 8, 8, 3 so thats why get the gap coz that gap needs to be closed instead of doing it one by one
            cost = count * gap  #instead odf count, i+1 can be used but lets go. 

            if k >= cost:  #if k = 5 and cost is 2 then just jump to 8,8,3.
                k -= cost
            else:
                level, rem = divmod(k, count) #gives out a quotient and rem value so now k = 3 and count = 2 then quo is 1 and rem = 1

                for j in range(count):
                    diff[j] = diff[i] - level   
                    """ in 0  1   2.    For [8, 8, 3] with k = 3, we have:

                            count = 2
                            level, rem = divmod(3, 2)
                            # level = 1, rem = 1

                            The two largest values are both 8.

                            Reduce both by level = 1: [7, 7, 3]

                            Reduce the first one by one extra because rem = 1: [6, 7, 3]

                            So the result is [6, 7, 3].

                            """
                    if j < rem:                
                        diff[j] -= 1
                k = 0
                break
        return sum(d * d for d in diff)
