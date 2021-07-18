// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

//Back-end complete function Template for C++

class Solution{
  public:
    long maximum_sum(int N,vector<int> A,int K)
    {
       // Your code here
       unordered_map<int,int> m;
       long sum=0;
       for(int i=0;i<N;i++){
           m[A[i]]++;
       }
       priority_queue<pair<int,int>> pq;
       for( auto i:m){
           pq.push({i.second,i.first});
       }
       while(K--){
           pair<int,int> p;
           p = pq.top();
           pq.pop();
           p.first--;
           sum+=p.second;
           if(p.first){
               pq.push(p);
           }
       }
       return sum;
    }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        vector<int>v(n,0);
        
        for(int i=0;i<n;i++)
        cin>>v[i];
        Solution obj;
        cout<< obj.maximum_sum(n,v,k)<<endl;
    }
    return 0;
}
  // } Driver Code Ends