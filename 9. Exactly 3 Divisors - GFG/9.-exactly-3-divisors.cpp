// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    bool isprime(int a){
        for(int i=2;i*i<=a;i++)
        if(a%i==0)
        return false;
        return true;
    }
    int exactly3Divisors(int N)
    {
        int c=0;
        //Your code here
        if(N<4)
        return 0;
        for(int i=2;i*i<=N;i++)
        if(isprime(i))
        c+=1;
    return c;
    }
};

// { Driver Code Starts.


int main()
 {
    int T;
    
    //taking testcases
    cin>>T;
    while(T--)
    {
        int N;
        
        //taking N
        cin>>N;
        Solution ob;
        //calling function exactly3Divisors()
        cout<<ob.exactly3Divisors(N)<<endl;
    }
	return 0;
}  // } Driver Code Ends