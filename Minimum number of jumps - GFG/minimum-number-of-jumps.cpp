// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
        // Your code here
        int minjump=0,end=0,reach=0;
        for(int i=0;i<n-1;i++){
            if(i+arr[i]>=reach){
                reach = i+arr[i];
            }
            if(i==end){
                end=reach;
                minjump++;
            }
            if(end>=n-1){
                break;
            }
        }
        if(end<n-1) return -1;
        return minjump;
    }
};


// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}
  // } Driver Code Ends