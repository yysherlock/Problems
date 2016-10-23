#ifdef _CHAP2_
#define _CHAP2_

#include <iostream>
//using namespace std;

struct node {
    int data;
    node* next;
};

extern node* kthToLast(node* head, int k);
extern node* init(int a[], int n);
extern void print(node *head);

#endif
