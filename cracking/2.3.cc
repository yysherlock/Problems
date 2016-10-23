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

bool deleteNode(node* target){
    if (target==NULL||target->next==NULL) return false;
    // a->b->c->d->e to a->b->c->e
    node *tmp = target->next;
    target->next = tmp->next;
    target->data = tmp->data;
    delete tmp;
    return true;
}

void print(node *head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

int main(){
    int n = 10;
    int a[] = {
        9, 2, 1, 3, 5, 6, 2, 6, 3, 1
    };
    node *head = init(a, n);
    node *c = head;
    int cc = 3;
    for(int i=1; i<cc; ++i) c = c->next;
    print(head);
    if(deleteNode(c))
        print(head);
    else
        cout<<"failure"<<endl;

    return 0;
}
