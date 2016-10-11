#include <iostream>
using namespace std;

typedef struct node {
  int data;
  node* next;
}node;

node* init(int a[], int n){
    node* head, *p;
    for (int i=0; i<n; ++i){
      node* nd = new node();
      nd->data = a[i];
      if (i==0){
        head = p = nd;
        continue;
      }
      p->next = nd;
      p = nd;
    }
    return head;
}

void removeDuplicate(node* head){
  if(head==NULL) return;
  node *p, *q, *c = head;
  while(c){
    int cur = c->data;
    p = c; // p is the runner of q, always 1 step before q
    q = p->next;
    while(q){
        if(q->data==cur) { // delete q node
          p->next = q->next;
          q = p->next;
        } else {
          p = p->next;
          q = q->next;
        }
    }
    c = c->next;
  }
}

void print(node *head){
    while(head){
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

int main(){
  int a[] = {3, 2, 1, 3, 5, 6, 2, 6, 3, 1 };
  node* l = init(a,10);
  removeDuplicate(l);
  print(l);
  return 0;
}
