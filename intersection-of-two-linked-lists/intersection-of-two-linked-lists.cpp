/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int n=0,s=0;
        ListNode* A = headA;
        ListNode* B = headB;
        while(A!=NULL){
            n++;
            A = A->next;
        }
        while(B!=NULL){
            s++;
            B=B->next;
        }
        int d = abs(n-s);
        ListNode* a = headA;
        ListNode* b = headB;
        if(n>s){
            for(int i=0;i<d;i++){
                a = a->next;
            }
        }
        else{
            for(int i=0;i<d;i++){
                b = b->next;
            }
        }
        while(a && b){
            if(a==b){
                return a;
            }
            a = a->next;
            b = b->next;
        }
        return NULL;
    }
};