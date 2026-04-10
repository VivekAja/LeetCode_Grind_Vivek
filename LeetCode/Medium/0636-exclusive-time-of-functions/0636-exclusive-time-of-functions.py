class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        funcstack = []
        exe_time= [0]*n
        previous_timestamp = 0

        for log in logs:
            func, op, timest = log.split(":")
            func = int(func)
            cur_time = int(timest)

            if op == "start":
                if funcstack:
                    top_func = funcstack[-1]
                    exe_time[top_func] += cur_time- previous_timestamp 
                funcstack.append(func)
                previous_timestamp = cur_time
            else:
                end_func = funcstack.pop()
                exe_time[end_func] += cur_time- previous_timestamp + 1
                previous_timestamp = cur_time + 1
        return exe_time

