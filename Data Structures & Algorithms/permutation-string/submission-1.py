from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if lens1 > lens2:
            return False

        seens1 = defaultdict(int)
        seens2 = defaultdict(int)

        for alp in s1:
            seens1[alp] += 1

        left = 0
        for right in range(lens2):
            seens2[s2[right]] += 1

            if right - left + 1 > lens1:
                seens2[s2[left]] -= 1
                if seens2[s2[left]] == 0:
                    del seens2[s2[left]]
                left += 1

            if seens2 == seens1:
                return True

        return False