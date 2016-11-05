#include <iostream>
#include <stack>
#include <queue>
using namespace std;

template <typename T>
stack<T> Ssort(stack<T> s) {
    stack<T> t;
    while (!s.empty()){
        T data = s.top();
        s.pop();
        while (!t.empty() && data > t.top()) {
            s.push(t.top());
            t.pop();
        }
        t.push(data);
    }
    while (!t.empty()){
        s.push(t.top());
        t.pop();
    }
    return s;
}

template <typename T>
void Qsort(stack<T> &s){
    priority_queue<T, vector<T>, greater<T> > q;
    while (!s.empty()){
        q.push(s.top());
        s.pop();
    }
    while (!q.empty()){
        s.push(q.top());
        q.pop();
    }
}

int main(){
    srand((unsigned)time(0));
    stack<int> s;

    for(int i=0; i<10; ++i){
        int val = rand()%100;
        s.push(val);
        cout << val << " ";
    }
    cout << endl;
    //s = Ssort<int>(s);
    Qsort<int>(s);
    while(!s.empty()){
        cout<<s.top()<<" ";
        s.pop();
    }
    cout << endl;

    return 0;
}
