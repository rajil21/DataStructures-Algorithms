class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        for i in range(len(items)):
            if((ruleKey=="type" and ruleValue==items[i][0]) or ("color"==ruleKey and ruleValue==items[i][1]) or("name"==ruleKey and ruleValue==items[i][2])):
                c+=1
        return c
        