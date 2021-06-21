class Solution:
    #your task is to complete this function
    #Function should return the required answer
    #You are not allowed to convert string to integer
    def remainderWith7(self, st):
        #Code here
        r=0
        for i in range(len(st)):
            r = r*10 + (ord(st[i])-ord('0'))
            r%=7
        return r

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        ob=Solution()
        print(ob.remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends