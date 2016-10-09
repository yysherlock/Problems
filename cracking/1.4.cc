#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isAnagram1(string s, string t){
    if(s==t) return true;
    if(s.length() != t.length()) return false;

    sort(&s[0], &s[0]+s.length());
    sort(&t[0], &t[0]+t.length());
    if (s==t) return true;
    else return false;
}

bool isAnagram2(string s, string t){
    if(s==t) return true;
    if(s.length() != t.length()) return false;

    int len = s.length();
    int c[256];
    memset(c, 0, sizeof(c));
    for (int i=0; i<len; ++i){
        ++c[(int)s[i]];
        --c[(int)t[i]]; // finesse!!
    }
    for (int i=0; i<256; i++){
        if(c[i] != 0) return false;
    }
    return true;
}

int main(){
    string s = "aaabbb";
    string t = "ababab";
    cout<<isAnagram1(s, t)<<endl;
    cout<<isAnagram2(s, t)<<endl;
    return 0;
}
