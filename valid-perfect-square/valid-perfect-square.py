class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(int(sqrt(num))**2==num):
            return True
        return False
        