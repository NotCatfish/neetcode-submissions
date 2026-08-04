from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sdict=defaultdict(int)
        tdict=defaultdict(int)
        left=0
        answer=[]
        flag=1

        #store s value in dictionary to check with t dictionary to see if it matches
        for  x in t:
            tdict[x]+=1

        #store t values in dictionary
        for right in range(len(s)):
            sdict[s[right]]+=1

            #check if tdict has all values of sdict
            while all(k in sdict and v <= sdict[k] for k, v in tdict.items()):
                #if true check the length of tdict and the current shortest substring
                #for the first time when answer is []
                current_length = right - left + 1
                if flag==1:
                    answer = list(s[left : right + 1])
                    flag=0
                #when its not []
                elif current_length < len(answer):
                    answer = list(s[left : right + 1])

                sdict[s[left]] -= 1
                left += 1

        return "".join(answer)
                        
                    