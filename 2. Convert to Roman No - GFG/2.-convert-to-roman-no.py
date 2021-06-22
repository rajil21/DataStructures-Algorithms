#Your task is to complete this function 
#Your function should return a String
def convertRoman(n):
    #Code here
    L= ['I','V','X','L','C','D','M']
    s=''
    if(n>=1000):
        s+= 'M'*(n//1000)
        n = n%1000
    if(n>=900):
        s+='CM'
        n=n%900
    if(n>=500):
        s+='D'*(n//500)
        n=n%500
    if(n>=400):
        s+='CD'
        n=n%400
    if(n>=100):
        s+='C'*(n//100)
        n%=100
    if(n>=90):
        s+='XC'
        n%=90
    if(n>=50):
        s+='L'*(n//50)
        n%=50
    if(n>=40):
        s+='XL'
        n%=40
    if(n>=10):
        s+='X'*(n//10)
        n%=10
    if(n==9):
        s+='IX'
        n%=9
    if(n>=5):
        s+='V'*(n//5)
        n%=5
    if(n==4):
        s+='IV'
        n%=4
    if(n>=1):
        s+='I'*(n)
    return s
        

#{ 
#  Driver Code Starts
#Your Code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends