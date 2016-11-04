#include <iostream>
#include <stack>
using namespace std;

void hanoi(int n, char src, char bri, char dst){
    if (n == 1){
        cout << "plate " << n << ": " << src << "->" << dst << endl;
        return;
    }
    hanoi(n-1, src, dst, bri);
    cout << "plate " << n << ": " << src << "->" << dst << endl;
    hanoi(n-1, bri, src, dst);
}

struct op {
    int begin, end;
    char src, bri, dst;
    op(){

    }
    op(int pbegin, int pend, char psrc, char pbri, char pdst):
        begin(pbegin),end(pend),src(psrc),bri(pbri),dst(pdst){

        }
};

void hanoi1(int n, char src, char bri, char dst){
    stack<op> st;
    op tmp;
    st.push(op(1, n, src, bri, dst));
    while(!st.empty()){
        tmp = st.top();
        st.pop();
        if (tmp.begin != tmp.end){
            st.push(op(tmp.begin, tmp.end-1, tmp.bri, tmp.src, tmp.dst));
            //st.push(tmp);
            st.push(op(tmp.end, tmp.end, tmp.src, tmp.bri, tmp.dst));
            st.push(op(tmp.begin, tmp.end-1, tmp.src, tmp.dst, tmp.bri));
        } else {
            cout << "plate " << tmp.begin << ": " << tmp.src << "->" << tmp.dst << endl;
        }
    }
}

int main(){
    hanoi(3, 'A', 'B', 'C');
    cout << endl;
    hanoi1(3, 'A', 'B', 'C');
    return 0;
}
