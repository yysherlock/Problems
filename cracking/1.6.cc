#include <iostream>
#include <string>
using namespace std;

string compress(string s){
    string re = "";
    int len = s.length();
    if (s=="") return s;
    char cur = s[0];
    int count = 1, i = 1;
    while(i < len){
        while(s[i] == cur) {
            ++count;
            ++i;
        }
        re = re + cur + to_string(count);
        cur = s[i++];
        count = 1;
    }

    if (re.length() >= s.length()) return s;
    return re;
}

int main(){
    string s1 = "aabcccccaaa";
    cout << compress(s1) << endl;

    return 0;
}
