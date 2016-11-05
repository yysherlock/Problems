#include <iostream>
#include <stack>
using namespace std;

void foo(stack<int> &s){
    s.push(100);
}

int main(){
    stack<int> s;
    for (int i=0; i<10; ++i)
        s.push(i);
    cout << s.size() << endl;
    foo(s);
    cout << s.size() << endl;

    return 0;
}
