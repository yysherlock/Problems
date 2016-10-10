#include <iostream>

using namespace std;

char* replace(char* str){
    char* cur = str;
    int spaces_cnt = 0;
    while(*cur){
        if(*cur==' ') ++spaces_cnt;
        ++cur;
    }
    --cur;

    int len = strlen(str) + 2*spaces_cnt;
    char* tend = str + len - 1;
    *(tend+1) = '\0';
    while(cur >= str){
        if(*cur == ' '){
            *tend-- = '0';
            *tend-- = '2';
            *tend-- = '%';
        } else {
            *tend-- = *cur;
        }
        --cur;
    }
    return str;
}

int main(){
    const int len = 100;
    char c1[len] = "ab cd ef g"; // if len is too small,
                                // there will be "Abort trap" error.
    char c2[len] = "a ";
    cout << replace(c1) << endl;
    cout << replace(c2) << endl;
    return 0;
}
