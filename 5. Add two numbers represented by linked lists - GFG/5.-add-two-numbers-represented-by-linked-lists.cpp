// { Driver Code Starts
// driver

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

/* Linked list Node */
struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

struct Node* buildList(int size)
{
    int val;
    cin>> val;
    
    Node* head = new Node(val);
    Node* tail = head;
    
    for(int i=0; i<size-1; i++)
    {
        cin>> val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    cout<< endl;
}


 // } Driver Code Ends
/* node for linked list:

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    //Function to add two numbers represented by linked list.
    
    Node* reverseLL(Node* head){
        Node* curr = head;
        Node *prev = NULL,*next=NULL;
        while(curr!=NULL){
            next = curr->next;
            curr->next= prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
/* Adds contents of two linked lists and
return the head node of resultant list */
    Node* addTwoLists(Node* first, Node* second)
    {
        if(first==NULL) return second;
        if(second==NULL) return first;
        first = reverseLL(first);
        second = reverseLL(second);
        int sum,carry=0,f,s;
        Node* start=NULL,*end=NULL;
        while(first!=NULL || second!=NULL){
            f = (first)?first->data:0;
            s =  (second)?second->data:0;
            sum = carry + f+s;
            carry = (sum>=10)?1:0;
            sum%=10;
            if(start==NULL){
                start = new Node(sum);
                end = start;
            }
            else{
                end->next = new Node(sum);
                end =end->next;
            }
            if(first) first = first->next;
            if(second) second = second->next;
        }
        if(carry>0){
            end->next = new Node(carry);
        }
        start = reverseLL(start);
        return start;
    }
};


// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        
        cin>>n;
        Node* first = buildList(n);
        
        cin>>m;
        Node* second = buildList(m);
        Solution ob;
        Node* res = ob.addTwoLists(first,second);
        printList(res);
    }
    return 0;
}
  // } Driver Code Ends