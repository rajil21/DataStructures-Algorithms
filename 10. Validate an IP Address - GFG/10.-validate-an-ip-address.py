#User function Template for python3

def isValid(s):
    #code here
    L = s.split('.')
    if(len(L)!=4):
        return False
    for i in L:
        if(not(i.isnumeric())):
            return False
        a = int(i)
        if(not(a>=0 and a<=255)):
            return False
        if(i[0]=='0' and len(i)!=1):
            return False
    return True
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends