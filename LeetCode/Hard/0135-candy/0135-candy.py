class Solution:
    def candy(self, ratings: List[int]) -> int:
        # candy = 0
        # for i in range(len(ratings)):
        #     if i == 0 :
        #         if ratings[i] > ratings[i+1]:
        #             candy +=2
        #         else:
        #             candy += 1
        #     elif i < len(ratings)-1:
        #         if ratings[i] > ratings[i+1] or ratings[i] > ratings[i-1]:
        #             candy +=2
        #         else:
        #             candy += 1
        #     elif i == len(ratings)-1:
        #         if ratings[i] > ratings[i-1]:
        #             candy +=2
        #         else:
        #             candy += 1
        # return candy

        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)
        return sum(candy)