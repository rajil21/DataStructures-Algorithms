// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to find largest rectangular area possible in a given histogram.
    long long getMaxArea(long long arr[], int n)
    // {
    //     // Your code here
    //     stack<int> s;
    //     long long area;
    //     long long ma =-1;
    //     int temp;
    //     for(int i=0;i<n;i++){
    //         while(!s.empty() && arr[s.top()]>=arr[i]){
    //             temp = arr[s.top()];
    //             s.pop();
    //             area = temp*((!s.empty())?i-s.top()-1:i);
    //             if(area>ma) ma = area;
    //         }
    //         s.push(i);
    //     }
    //     while(!s.empty()){
    //         temp = arr[s.top()];
    //         s.pop();
    //         area = temp*((!s.empty())?n-s.top()-1:n);
    //         if(area>ma) ma = area;
    //     }
    //     return ma;
    // }
    {
        // Your code here
        stack<int>s;
        long long res=0;
        long long curr=0;
        for(int i=0;i<n;i++) { while(s.empty()==false && arr[s.top()]>=arr[i])
            {
                int tp=s.top();
                s.pop();
                curr= arr[tp]*(s.empty()?i:(i-s.top()-1));
                res=max(curr,res);
            }
            s.push(i);
        }
        while(s.empty()==false)
        {
            int tp=s.top();
            s.pop();
            curr=arr[tp]*(s.empty()?n:(n-s.top()-1));
            res=max(res,curr);
        }
        return res;
    }
};


// { Driver Code Starts.

int main()
 {
    long long t;

    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        long long arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        Solution ob;
        cout<<ob.getMaxArea(arr, n)<<endl;
    
    }
	return 0;
}
  // } Driver Code Ends