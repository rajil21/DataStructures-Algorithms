// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


class Solution
{
    public:
    //Function to find maximum of minimums of every window size.
    vector <int> maxOfMin(int arr[], int n)
    {
        // Your code here
        int left[n],right[n];
        stack<int> s;
        for(int i=0;i<n;i++){
            left[i]=-1;
            right[i]=n;
        }
        for(int i=0;i<n;i++){
            while(!s.empty() && arr[s.top()]>=arr[i])
            s.pop();
            if(!s.empty()) left[i]=s.top();
            s.push(i);
        }
        while(!s.empty()) s.pop();
        for(int i=n-1;i>=0;i--){
            while(!s.empty() && arr[s.top()]>=arr[i])
            s.pop();
            if(!s.empty()) right[i]=s.top();
            s.push(i);
        }
        vector<int> mom(n+1,0);
        int len;
        for(int i=0;i<n;i++){
            len = right[i]-left[i]-1;
            mom[len] = max(mom[len],arr[i]);
        }
        for(int i=n-1;i>=0;i--){
            mom[i]=max(mom[i],mom[i+1]);
        }
        mom.erase(mom.begin());
        return mom;
        
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution ob;
        vector <int> res = ob.maxOfMin(a, n);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends