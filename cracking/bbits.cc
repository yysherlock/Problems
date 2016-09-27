#include <iostream>
#include <string>

using std::cout;
using std::endl;

bool getBit(int num, int i){
    return num & (1<<i);
}

int main(){
    //cout << ~(size_t)0 << endl;
    //cout << ~(size_t)0 << 2 << endl;
    unsigned int max = ~0; // 32bits of 1
    cout << max << endl;
    cout << ~(size_t)0 << endl; // 64bits of 1
    cout << (size_t)~0 << endl;
    cout << getBit(4,1) << " " <<getBit(4,0) << endl;    
    return 0;
}
