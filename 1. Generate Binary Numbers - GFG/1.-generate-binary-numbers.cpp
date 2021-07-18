// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;



 // } Driver Code Ends

//Function to generate binary numbers from 1 to N using a queue.
vector<string> generate(int N)
{
	// Your code here
	queue<string> q;
	vector<string> numbers;
	q.push("1");
	while(N--){
	    string c = q.front();
	    numbers.push_back(c);
	    q.pop();
	    q.push(c+"0");
	    q.push(c+"1");
	}
	return numbers;
}


// { Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		vector<string> ans = generate(n);
		for(auto it:ans) cout<<it<<" ";
		cout<<endl;
	}
	return 0;
}  // } Driver Code Ends