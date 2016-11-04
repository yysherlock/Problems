#include <iostream>
using namespace std;

class Stack {
    public:
        Stack(int size=1000){
            this->size = size;
            buf = new int[size];
            cur = -1;
        }
        ~Stack(){
            delete[] buf;
        }
        int top(){
            if(!this->empty())
                return buf[cur];
            else return 0;
        }
        bool empty(){
            return cur==-1;
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

class StackWithMin {
    public:
        int min(){
            return s2.top();
        }
        void push(int val){
            s1.push(val);
            if(val <= s2.top()){
                s2.push(val);
            }
        }
        void pop(){
            if (s1.top() == s2.top()){
                s2.pop();
            }
            s1.pop();
        }

        int top(){
            return s1.top();
        }

    private:
        Stack s1, s2;
};

int main(){

    StackWithMin mystack;
	for(int i=0; i<20; ++i)
		mystack.push(i);
	cout<<mystack.min()<<" "<<mystack.top()<<endl;
	mystack.push(-100);
	mystack.push(-100);
	cout<<mystack.min()<<" "<<mystack.top()<<endl;
	mystack.pop();
	cout<<mystack.min()<<" "<<mystack.top()<<endl;

    return 0;
}
