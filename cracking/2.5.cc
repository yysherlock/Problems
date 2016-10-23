#include <iostream>
using namespace std;

struct node {
    int data;
    node* next;
};

node* init(int a[], int n){
    node *head, *p;
    for (int i=0; i<n; ++i){
        node* nd = new node();
        nd->data = a[i];
        if(i==0) {
            p = head = nd;
        } else {
            p->next = nd;
            p = nd;
        }
    }
    return head;
}


void print(node *head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

node* addition1(node* head1, node* head2){
    // reverse store the number in the list
    node *result, *prev;
    result = prev = NULL;
    node *p = head1;
    node *q = head2;
    int c = 0;
    while(p || q || c>0){
        node* nd = new node();
        if(result==NULL) {
            result = prev = nd;
        } else {
            prev->next = nd;
        }
        int a = p ? p->data : 0;
        int b = q ? q->data : 0;
        int s = a + b + c;
        c = s / 10;
        nd->data = s % 10;
        prev = nd;
        prev->next = NULL;
        if(p) p = p->next;
        if(q) q = q->next;
    }
    return result;
}


node* kthToLast(node *head, int k){
    node *p, *q;
    p = q = head;
    for(int i=1; i<k; ++i){
        if (q==NULL) return NULL;
        q = q->next;
    }
    while (q->next){
        q = q->next;
        p = p->next;
    }
    return p;
}

node* findtail(node* head){
    node *p = head;
    if (p==NULL||p->next==NULL) return head;
    while(p->next){
        p = p->next;
    }
    return p;
}


node* reverseList(node* head){
    node *tail, *prev, *res=NULL;
    while ( (tail=findtail(head)) != head ){
        node* nd = new node();
        if(res==NULL) {
            res = prev = nd;
        } else {
            prev->next = nd;
        }
        nd->data = tail->data;
        prev = nd;
        prev->next = NULL;

        node* pp = kthToLast(head, 2);
        tail->next = head;
        pp->next = NULL;
    }
    prev->next = head;
    return res;
}

node* addition2(node* head1, node* head2){
    // store the number in the list
    node *h1 = reverseList(head1);
    node *h2 = reverseList(head2);
    return addition1(h1,h2);
}

int main(){
    int n = 5;
    int a[] = {
        1, 2, 9, 9, 3
    };
    int m = 3;
    int b[] = {
        9, 9, 2
    };

    node *p = init(a, n);
    node *q = init(b, m);
    p = reverseList(p);
    q = reverseList(q);
    if(p) print(p);
    if(q) print(q);
//    node *res = addition1(p,q);
    node *res = addition2(p, q);

    if(res) print(res);
    //*/

    return 0;
}
