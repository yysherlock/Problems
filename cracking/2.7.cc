#include <iostream>
using namespace std;

struct node {
    int data;
    node* next;
};


void print(node *head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

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

bool listEqual(node* h1, node* h2){
    node *p = h1;
    node *q = h2;
    while(true){
        if(p==NULL && q==NULL) break;
        else if(p==NULL && q!=NULL) return false;
        else if(p!=NULL && q==NULL) return false;
        if(p->data != q->data) return false;
        p = p->next;
        q = q->next;
    }
    return true;
}

node* copyList(node* head){
    node *p = head;
    node *nhead = NULL;
    node *prev = NULL;
    while(p){
        node *nd = new node();
        nd->data = p->data;
        if(prev==NULL) nhead = prev = nd;
        else prev->next = nd;
        prev = nd;
        p = p->next;
    }
    return nhead;
}

bool palindromic(node *head){
    node *nhead = copyList(head);
    node *rev = reverseList(head);
    return listEqual(nhead, rev);
}

int main(){
    int n = 7;
    int a[] = {
        1, 2, 3, 4, 3, 2, 1
    };
    node *head = init(a, n);
    cout << palindromic(head) << endl;
    //print(head);
    //print(reverseList(head));
    return 0;
}
