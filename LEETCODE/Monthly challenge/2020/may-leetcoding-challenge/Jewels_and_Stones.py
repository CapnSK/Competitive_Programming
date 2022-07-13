class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels={c:True for c in J}
        cnt=0
        for c in S:
            if c in jewels:
                cnt+=1
        return cnt