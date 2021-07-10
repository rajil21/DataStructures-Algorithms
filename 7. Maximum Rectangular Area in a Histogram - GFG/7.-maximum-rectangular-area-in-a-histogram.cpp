// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to find largest rectangular area possible in a given histogram.
    long long getMaxArea(long long arr[], int n)
    {
        // Your code here
        stack<int> s;
        long long area;
        long long ma =-1;
        int temp;
        for(int i=0;i<n;i++){
            while(!s.empty() && arr[s.top()]>=arr[i]){
                temp = s.top();
                s.pop();
                area = arr[temp]*((!s.empty())?i-s.top()-1:i);
                if(area>ma) ma = area;
            }
            s.push(i);
        }
        while(!s.empty()){
            temp = s.top();
            s.pop();
            area = arr[temp]*((!s.empty())?n-s.top()-1:n);
            if(area>ma) ma = area;
        }
        return ma;
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