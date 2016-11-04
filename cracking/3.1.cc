#include <iostream>
using namespace std;

struct node {
    int val, preIdx;
    bool empty;
    node(){
        empty = true;
    }
};

class Stack3{
    public:
        Stack3(int totalSize = 900){
            this->totalSize = totalSize;
            buf = new node[totalSize];
            ptop[0] = ptop[1] = ptop[2] = -1;
            cur = 0;
        }
        ~Stack3(){
            delete[] buf;
        }

        void push(int stack, int val){
            buf[cur].val = val;
            buf[cur].preIdx = ptop[stack];
            buf[cur].empty = false;
            ptop[stack] = cur;

            // update cur
            for(int i=cur+1; i<totalSize; ++i){
                if (buf[i].empty) {
                    cur = i;
                    break;
                }
            }

        }

        void pop(int stack){
            if (cur > ptop[stack]){
                cur = ptop[stack];
            }
            buf[ptop[stack]].empty = true;
            ptop[stack] = buf[ptop[stack]].preIdx;
        }

        int top(int stack){
            return buf[ptop[stack]].val;
        }

        bool empty(int stack){
            return ptop[stack]==-1;
        }

    private:
        node *buf;
        int totalSize;
        int ptop[3];
        int cur;
};

int main(){
    Stack3 s;
    for(int i=0; i<10; ++i) s.push(0, i);
    for(int i=0; i<20; ++i) s.push(1, i);
    for(int i=0; i<110; ++i) s.push(2, i);
    for(int i=0; i<3; ++i) cout << s.top(i) << " ";
    cout << endl;

    for(int i=0; i<3; ++i){
        s.pop(i);
        cout << s.top(i) << " ";
    }

    s.push(0, 111);
    s.push(1, 222);
    s.push(2, 333);
    for(int i=0; i<3; ++i)
        cout << s.top(i) << " ";
    cout << endl;
    return 0;
}
