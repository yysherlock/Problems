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

node* circularStart(node *head){
    node *i, *j;
    i = head; j = head->next;
    int circular_start = 0;
    while (i!=j){
        i = i->next;
        j = j->next->next;
        ++circular_start;
    }
    node *start = head;
    for(int i=0; i<circular_start; ++i){
        start = start->next;
    }
    return start;
}

node* findtail(node* head){
    node *p = head;
    if (p==NULL||p->next==NULL) return head;
    while(p->next){
        p = p->next;
    }
    return p;
}

int main(){
    int n = 5;
    int a[] = {
        1, 2, 3, 4, 5
    };
    node *head = init(a, 5);
    int pos = 2;
    node *start = head;
    for(int i=0; i<pos; ++i) start=start->next;
    findtail(head)->next = start;

    node *findstart = circularStart(head);
    cout << findstart->data << endl;
    cout << (findstart==start) << endl;
    return 0;
}
