#include <iostream>
#include <string>
using namespace std;

bool isUnique1(string s){
    bool a[256];
    memset(a, 0, sizeof(a)); // initialize with 0s
    int len = s.length();
    for (int i=0; i < len; ++i){
        int v = (int)s[i];
        if(a[v]) return false;
        else a[v] = true;
    }
    return true;
}

bool isUnique2(string s){
    //8 ints, 256 bits for ascii characters
    int a[8];
    memset(a, 0, sizeof(a));
    int len = s.length();
    for (int i=0; i<len; ++i){
        int idx = (int)s[i]/32;
        int pos = (int)s[i]%32;
        if(a[idx] & (1<<pos)) return false;
        else a[idx] |= (1<<pos);
    }
    return true;
}

int main(){
    string s1 = "hello world";
    string s2 = "abcdefghijklmnopqrstuvwxyz1234567890";
    cout<<isUnique1(s1)<<" "<<isUnique1(s2)<<endl;
    cout<<isUnique2(s1)<<" "<<isUnique2(s2)<<endl;

    return 0;
}
