// { Driver Code Starts
// C++ implementation to convert infix expression to postfix
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends

class Solution
{
    public:
    //Function to convert an infix expression to a postfix expression.7
    int pri(char c){
    if(c=='^') return 3;
    else if (c=='/' || c=='*') return 2;
    else if (c=='+' || c=='-') return 1;
    else return -1;
}
    string infixToPostfix(string infix)
    {
        stack<int> s;
        string postfix;
        for(int i=0;infix[i];i++){
            char c = infix[i];
            if((c>='a' && c<='z') ||(c>='A' && c<='Z'))
            postfix+=c;
            else if(c=='(')
            s.push(c);
            else if(c==')'){
                while(s.top()!='('){
                    postfix+=s.top();
                    s.pop();
                }
                s.pop();
            }
            else{
                while(!s.empty() && pri(c)<=pri(s.top())){
                    postfix+=s.top();
                    s.pop();
                }
                s.push(c);
            }
        }
        while(!s.empty()){
            postfix+=s.top();
            s.pop();
        }
        return postfix;
    }
};


// { Driver Code Starts.
//Driver program to test above functions
int main()
{
    int t;
    cin>>t;
    cin.ignore(INT_MAX, '\n');
    while(t--)
    {
        string exp;
        cin>>exp;
        Solution ob;
        cout<<ob.infixToPostfix(exp)<<endl;
    }
    return 0;
}
  // } Driver Code Ends