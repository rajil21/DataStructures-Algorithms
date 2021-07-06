// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node *next, *prev;
	
	Node (int x){
	    data = x;
	    next = NULL;
	    prev = NULL;
	}
};


 // } Driver Code Ends
/*
Structure of the node of the list is as
struct Node
{
	int data;
	struct Node *next, *prev;
	Node (int x){
	    data = x;
	    next = prev = NULL;
	}
}; */
// Node *merge(Node *first, Node *second)
// {
//     // If first linked list is empty
//     if (!first)
//         return second;
 
//     // If second linked list is empty
//     if (!second)
//         return first;
 
//     // Pick the smaller value
//     if (first->data < second->data)
//     {
//         first->next = merge(first->next,second);
//         first->next->prev = first;
//         first->prev = NULL;
//         return first;
//     }
//     else
//     {
//         second->next = merge(first,second->next);
//         second->next->prev = second;
//         second->prev = NULL;
//         return second;
//     }
// }
// Node *split(Node *head)
// {
//     Node *fast = head,*slow = head;
//     while (fast->next && fast->next->next)
//     {
//         fast = fast->next->next;
//         slow = slow->next;
//     }
//     Node *temp = slow->next;
//     slow->next = NULL;
//     return temp;
// }
// // Function to do merge sort
// Node *mergeSort(Node *head)
// {
//     if (!head || !head->next)
//         return head;
//     Node *second = split(head);
 
//     // Recur for left and right halves
//     head = mergeSort(head);
//     second = mergeSort(second);
 
//     // Merge the two sorted halves
//     return merge(head,second);
// }


 Node *merge(Node* first,Node* second ){
    if(!first) return second;
    if(!second) return first;
    if(first->data<second->data){
        first->next = merge(first->next,second);
        first->next->prev = first;
        first->prev = NULL;
        return first;
    }
    else{
        second->next = merge(first,second->next);
        second->next->prev = second;
        second->prev = NULL;
        return second;
    }
}
Node *split( Node *head){
    Node *slow=head,*fast = head;
    while(fast->next&& fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    Node *s = slow->next;
    slow->next = NULL;
    return s;
}
 Node *mergesort( Node *head){
    if(!head || !head->next) return head;
    Node* second = split(head);
    head = mergesort(head);
    second = mergesort(second);
    return merge(head,second);
}

//Function to sort the given doubly linked list using Merge Sort.
 Node *sortDoubly( Node *head)
{
	// Your code here
	return mergesort(head);
}


// { Driver Code Starts.

void insert(struct Node **head, int data)
{
	struct Node *temp = new Node (data);
	if (!(*head))
		(*head) = temp;
	else
	{
		temp->next = *head;
		(*head)->prev = temp;
		(*head) = temp;
	}
}

void print(struct Node *head)
{
	struct Node *temp = head;
	while (head)
	{
		cout<<head->data<<' ';
		temp = head;
		head = head->next;
	}
	cout<<endl;
	while (temp)
	{
		cout<<temp->data<<' ';
		temp = temp->prev;
	}
	cout<<endl;
}

// Utility function to swap two integers
void swap(int *A, int *B)
{
	int temp = *A;
	*A = *B;
	*B = temp;
}


// Driver program
int main(void)
{
    long test;
    cin>>test;
    while(test--)
    {
        int n, tmp;
        struct Node *head = NULL;
        cin>>n;
        while(n--){
            cin>>tmp;
            insert(&head, tmp);
        }
        head = sortDoubly(head);
        print(head);
    }
	return 0;
}
  // } Driver Code Ends