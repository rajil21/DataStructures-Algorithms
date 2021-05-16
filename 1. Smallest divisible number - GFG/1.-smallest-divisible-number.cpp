// { Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
public:
    long long gcd(long long A,long long B){
        if(B==0){
            return A;
        }
        else{
            return gcd(B,A%B);
        }
    }
    long long getSmallestDivNum(long long n){
        // code here
        long long m = 1;
        for(int i=1;i<=n;i++)
        m = (((m*i))/gcd(i,m));
        return m;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<< ob.getSmallestDivNum(n)<<endl;
    }
    return 0;
}  // } Driver Code Ends