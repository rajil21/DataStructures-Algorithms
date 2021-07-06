// { Driver Code Starts
#include <iostream>
#include <cstdio>
using namespace std;
 
/* a node of the singly linked list */
struct node
{
    int data;
    struct node *next;
    
    node(int x){
        data = x;
        next = NULL;
    }
};

/* A utility function to insert a node at the beginning of linked list */
void push(struct node** head_ref, int new_data)
{
    /* allocate node */
    struct node* new_node = new node(new_data);
 
    /* link the old list off the new node */
    new_node->next = (*head_ref);
 
    /* move the head to point to the new node */
    (*head_ref)    = new_node;
}
 
/* A utility function to print linked list */
void printList(struct node *node)
{
    while (node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}
void quickSort(struct node **headRef);
int main()
{
	int t,n,x;
	cin>>t;
	while(t--){
		
        
        cin>>n;n=n-1;
		cin>>x;
        node *temp,*head = new node(x);
        temp=head;
        while(n--)
        {
			cin>>x;
          temp->next=new node(x);
          temp=temp->next;
			}
    
    quickSort(&head);
 
    printList(head);
 while(head!= NULL){
     temp=head;
     head=head->next;
     free(temp);
     
 }
	}
    return 0;
}// } Driver Code Ends


 
/* a node of the singly linked list 
struct node
{
    int data;
    struct node *next;
    
    node(int x){
        data = x;
        next = NULL;
    }
}; */

//you have to complete this function
struct node* partition(struct node *head,struct node* tail){
    node* pivot = head,*prev=head;
    node* curr = head->next;
    while(curr!=tail->next){
        if(curr->data<pivot->data){
            swap(prev->next->data,curr->data);
            prev=prev->next;
        }
        curr = curr->next;
    }
    swap(pivot->data,prev->data);
    return prev;
}
void quicksort(node* head,node* tail){
    if(head==tail||tail==NULL||head==NULL) return;
    struct node* pivot = partition(head,tail);
    quicksort(head,pivot);
    quicksort(pivot->next,tail);
}

void quickSort(struct node **headRef) {
    node* tail = *headRef;
    while(tail!=NULL && tail->next!=NULL){
        tail = tail->next;
    }
    quicksort(*headRef,tail);
}