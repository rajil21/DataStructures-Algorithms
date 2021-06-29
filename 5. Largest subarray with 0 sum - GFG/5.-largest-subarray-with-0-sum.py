#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    #Code here
    m=0
    d={}
    c=0
    for i in range(n):
        c+=arr[i]
        if(arr[i]==0 and m==0):
            m=1
        if(c==0):
            m=i+1
        if(c in d):
            m=max(m,i-d[c])
        else:
            d[c]=i
    return m

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends