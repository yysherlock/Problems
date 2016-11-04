#include <iostream>
#include <vector>
using namespace std;

class Stack {
    public:
        Stack(int size){
            this->size = size;
            buf = new int[size];
            cout << "allocate buf" << endl;
            cur = -1;
        }

        ~Stack(){
            //cout << "free buf" << endl;
            //delete[] buf;
        }

        int top(){
            return buf[cur];
        }

        bool empty(){
            return cur==-1;
        }

        bool full(){
            return cur==size-1;
        }

        void push(int val){
            buf[++cur] = val;
        }
        void pop(){
            --cur;
        }

    private:
        int size;
        int *buf;
        int cur;
};

class SetOfStacks {
    public:
        SetOfStacks(int sn, int sz){
            snum = sn;
            size = sz;
            cur = 0;
            for (int i=0; i<snum; ++i){
                //cout << "push " << i << " stack." << endl;
                ss.push_back(Stack(size));
            }
        }

        ~SetOfStacks(){
            ss.clear();
            vector<Stack>().swap(ss);
        }

        void push(int val){
            if(ss[cur].full()) ++cur;
            ss[cur].push(val);
        }

        void pop(){
            while(ss[cur].empty()) --cur;
            ss[cur].pop();
        }

        int top(){
            while(ss[cur].empty()) --cur;
            return ss[cur].top();
        }

        void popAt(int index){
            while(ss[index].empty()) --index;
            ss[index].pop();
        }
        bool empty(){
            while(cur!=-1 && ss[cur].empty()) --cur;
            if(cur==-1) return true;
            else return false;
        }
        bool full(){
            if (cur==snum-1) return ss[cur].full();
            else return false;
        }

    private:
        int snum;
        int size;
        int cur;
        vector<Stack> ss;
};

int main(){
    int size = 100;
    int snum = 10;
    SetOfStacks ss(snum, size);

    for(int i=0; i<3*size+1; ++i){
        ss.push(i);
    }

    for (int i = 0; i < 100; i++) {
        ss.popAt(0);
        //ss.popAt(1);
        ss.popAt(2);
    }
    ss.popAt(3);
    while(!ss.empty()){
		cout << ss.top() << endl;
		ss.pop();
	}
    return 0;
}
