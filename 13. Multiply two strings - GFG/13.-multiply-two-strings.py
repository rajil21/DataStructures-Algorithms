#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product
        if(s1[0]!='-' and s2[0]!='-' and s1.isnumeric() and s2.isnumeric()):
            return str(int(s1)*int(s2))
        elif(s1[0]!='-' and s2[0]=='-' and s1.isnumeric() and s2[1:].isnumeric()):
            return str(-1*int(s1)*int(s2[1:]))
        elif(s1[0]=='-' and s2[0]!='-' and s1[1:].isnumeric() and s2.isnumeric()):
            return str(-1*int(s1[1:])*int(s2))
        elif(s1[0]=='-' and s2[0]=='-' and s1[1:].isnumeric() and s2[1:].isnumeric()):
            return str(int(s1)*int(s2))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends