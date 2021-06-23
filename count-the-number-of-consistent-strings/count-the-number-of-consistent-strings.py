class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            o=0
            for j in range(len(words[i])):
                if(words[i][j] not in allowed):
                    o=1
                    break
            if(o==0):
                c+=1
        return c