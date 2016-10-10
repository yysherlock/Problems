#include <iostream>
#include <string>
using namespace std;

bool isRotation(string s1, string s2){
    string s = s2 + s2;
    if( s.find(s1) != string::npos ) return true;
    return false;
    // cout << string::npos << endl; // maximum value of size_t
}

int main(){
    string s1 = "waterbottle";
    string s2 = "erbottlewat";
    cout << isRotation(s1, s2) << endl;
    return 0;
}
