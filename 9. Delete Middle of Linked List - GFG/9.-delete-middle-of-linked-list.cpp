// { Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};

/* Function to get the middle of the linked list*/
struct Node *deleteMid(struct Node *head);
void printList(Node* node) 
{ 
	while (node != NULL) { 
		cout << node->data <<" "; 
		node = node->next; 
	}  
	cout<<"\n";
} 
int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;

		int data;
		cin>>data;
		struct Node *head = new Node(data);
		struct Node *tail = head;
		for (int i = 0; i < n-1; ++i)
		{
			cin>>data;
			tail->next = new Node(data);
			tail = tail->next;
		}
		head = deleteMid(head);
		printList(head); 
	}
	return 0; 
} 


// } Driver Code Ends


/* Link list Node:

struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};

*/

// Deletes middle of linked list and returns head of the modified list
Node* deleten(Node* head,int n){
    Node* temp = head;
    for(int i=0;i<n-2;i++){
        temp=temp->next;
    }
    Node* temp1= temp->next;
    temp->next = temp1->next;
    delete temp1;
    return head;
}
Node* deleteMid(Node* head)
{
    // Your Code Here
    if(head==NULL || head->next==NULL) return NULL;
    Node* t = head;
    int n=0;
    while(t!=NULL){
        n++;
        t = t->next;
    }
    if(n%2) return deleten(head,(n+1)/2);
    return deleten(head,(n/2)+1);
}