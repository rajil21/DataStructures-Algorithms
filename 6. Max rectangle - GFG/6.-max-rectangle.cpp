// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
#define MAX 1000


 // } Driver Code Ends
/*You are required to complete this method*/

class Solution{
  public:
  int histarea(int M[],int n)
  {
      stack <int> s;
      int maxarea = -1;
      int i=0;
      int val,area;
      while(i<n){
          if(s.empty() || M[s.top()]<=M[i]){
              s.push(i++);
          }
          else{
              val = M[s.top()];
              s.pop();
              int v1 = s.empty()?i:(i-s.top()-1);
              area = val*v1;
              if(area>maxarea) maxarea = area;
          }
      }
      while(!s.empty()){
          val = M[s.top()];
          s.pop();
          int v2 = (!s.empty())?(i-s.top()-1):i;
          area = val*v2;
          if(area>maxarea) maxarea = area;
      }
      return maxarea;
  }
    int maxArea(int M[MAX][MAX], int n, int m) {
        // Your code here
        int area = histarea(M[0],m);
        int are;
        for(int i=1;i<n;i++){
            for(int j=0;j<m;j++){
                if(M[i][j]==1) M[i][j]+=M[i-1][j];
            }
            are =  histarea(M[i],m);
            if(are>area) area =are;
        }
        return area;
    }
};


// { Driver Code Starts.
int main() {
    int T;
    cin >> T;

    int M[MAX][MAX];

    while (T--) {
        int n, m;
        cin >> n >> m;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> M[i][j];
            }
        }
        Solution obj;
        cout << obj.maxArea(M, n, m) << endl;
    }
}
  // } Driver Code Ends