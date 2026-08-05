class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for curr_day in range(len(temperatures)):
            curr_temp=temperatures[curr_day]

            while stack and curr_temp>temperatures[stack[-1]]:
                rescued_day=stack.pop()
                day_till_hot=curr_day-rescued_day
                result[rescued_day]=day_till_hot

            stack.append(curr_day)

        return result