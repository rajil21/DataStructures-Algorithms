// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
        // Your code here
        stack <int> s;
        for(int i=0;x[i];i++){
            if(x[i]=='(' || x[i]=='{' || x[i]=='[')
            {s.push(x[i]);
            continue;}
            if(s.empty()) return false;
            char ch = x[i];
            switch(ch){
                case '}': if ((s.top()=='(') || (s.top()=='[')) return false; break;
                case ')': if ((s.top()=='{') || (s.top()=='[')) return false; break;
                case ']': if ((s.top()=='(') || (s.top()=='{')) return false; break;
            }
            s.pop();
        }
        if(!s.empty()) return false;
        return true;
        
    }

};

// { Driver Code Starts.

int main()
{
   int t;
   string a;
   cin>>t;
   while(t--)
   {
       cin>>a;
       Solution obj;
       if(obj.ispar(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}  // } Driver Code Ends