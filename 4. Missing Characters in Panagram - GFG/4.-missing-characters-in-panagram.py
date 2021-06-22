#User function Template for python3

"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
class Solution:
    def missingPanagram(self, s):
        a="abcdefghijklmnopqrstuvwxyz"
        s=s.lower()
        q=''
        for i in range(len(a)):
            if(a[i] not in s):
                q+=a[i]
        if(len(q)==0):
            return -1
        return q


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        obj = Solution()
        print(obj.missingPanagram(s))
        t = t-1

# } Driver Code Ends