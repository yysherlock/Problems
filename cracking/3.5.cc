#include <iostream>
#include <stack>
#include <queue>
using namespace std;

template <typename T>
class MyQueue {

    public:
        MyQueue(){

        }
        ~MyQueue(){

        }

        void push(int val){
            spush.push(val);
        }

        void pop(){
            move(spush, spop);
            spop.pop();
        }

        T front(){
            move(spush, spop);
            return spop.top();
        }

        T back(){
            move(spop, spush);
            return spush.top();
        }

        bool empty(){
            return (spush.empty() && spop.empty());
        }

        void move(stack<T> &src, stack<T> &dst){
            if (dst.empty()) {
                while (!src.empty()) {
                    dst.push(src.top());
                    src.pop();
                }
            }
        }

        int size(){
            return spush.size() + spop.size();
        }

    private:
        stack<T> spush;
        stack<T> spop;
};

int main(){
    MyQueue<int> q;
    
	for(int i=0; i<10; ++i){
		q.push(i);
	}

	cout<<q.front()<<" "<<q.back()<<endl;
	q.pop();
	q.push(10);
	cout<<q.front()<<" "<<q.back()<<endl;
	cout<<q.size()<<" "<<q.empty()<<endl;

    return 0;
}
