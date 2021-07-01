// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// User function template for C++

class Solution{
    public:
    // arr[] : int input array of integers
    // k : the quadruple sum required
    vector<vector<int> > fourSum(vector<int> &arr, int k) {
        int n = arr.size();
        vector<vector<int>>res;
        sort(arr.begin(), arr.end());
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && arr[i - 1] == arr[i])
            continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && arr[j] == arr[j - 1])
                continue;
                int l = j + 1, h = n - 1;
                while (l < h) {
                    int sum = arr[i] + arr[j] + arr[l] + arr[h];
                    if (sum == k) {
                        res.push_back({arr[i], arr[j], arr[l], arr[h]});
                        l++;
                        h--;
                        while (l < h && arr[l] == arr[l - 1])
                        l++;
                        while (h > l && arr[h] == arr[h + 1])
                        h--;
                    }
                    else if (sum < k)
                        l++;
                    else
                        h--;
                }
            }
        }
        return res;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, i;
        cin >> n >> k;
        vector<int> a(n);
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        vector<vector<int> > ans = ob.fourSum(a, k);
        for (auto &v : ans) {
            for (int &u : v) {
                cout << u << " ";
            }
            cout << "$";
        }
        if (ans.empty()) {
            cout << -1;
        }
        cout << "\n";
    }
    return 0;
}  // } Driver Code Ends