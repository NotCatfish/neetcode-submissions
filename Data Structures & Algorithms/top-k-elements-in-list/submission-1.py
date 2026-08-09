import pandas as pd
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return pd.Series(nums).value_counts().head(k).index.tolist()