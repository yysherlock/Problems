#include <iostream>
#include <string>

using namespace std;

void removeDuplicate(char s[]){
    int len = strlen(s);
    if (len < 2) return ;
    bool a[256];
    memset(a, 0, sizeof(a));

    int pos = 0;
    for (int i=0; i<len; ++i){
        if(!a[s[i]]){ // pos <= i forever
            s[pos++] = s[i];
            a[s[i]] = true;
        }
    }
    s[pos] = '\0';
}

int main(){

    char ss1[] = "abcde";
    char ss2[] = "aaabbb";
    char ss3[] = "";
    char ss4[] = "abababc";
    char ss5[] = "ccccc";
    removeDuplicate(ss1);
    removeDuplicate(ss2);
    removeDuplicate(ss3);
    removeDuplicate(ss4);
    removeDuplicate(ss5);
    cout<<ss1<<" "<<ss2<<" "<<ss3<<" "<<ss4<<" "<<ss5<<endl;
    return 0;
}
