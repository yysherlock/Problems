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

node* partition(node* head, int x){
    if (head==NULL) return head;
    node *i, *j;
    i = j = head;
    while(j){
        if (j->data < x){
            // swap(i,j)
            int tmp = i->data;
            i->data = j->data;
            j->data = tmp;
            i = i->next;
        }
        j = j->next;
    }
    return head;
}

int main(){
    int n = 10;
    int a[] = {
        9, 2, 1, 3, 5, 6, 2, 6, 3, 1
    };
    node *head = init(a, n);
    print(head);
    print(partition(head, 5));
    return 0;
}
