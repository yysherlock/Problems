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

int main(){
    int n = 10;
    int a[] = {
        9, 2, 1, 3, 5, 6, 2, 6, 3, 1
    };
    node *head = init(a, n);
    node *p = kthToLast(head, 7);
    if(p) cout<<p->data<<endl;
    else cout<<"the length of link is not long enough"<<endl;
    return 0;
}
