#include <iostream>
#include <string>

using namespace std;

void reverse(char* str){
    int len = strlen(str);
    for (int i=0; i<len/2; ++i){
        char tmp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = tmp;
    }
}

void reverse1(char* str){
    char* end = str;
    while(*end){
        ++end;
    }
    --end;

    char tmp;
    while(str < end){
        tmp = *str;
        *str++ = *end;
        *end-- = tmp;
    }
}

void swap(char &a, char &b)
{
    a = a^b;
    b = a^b;
    a = a^b;
}

int main(){
    char str[] = "1234567890";
    char str1[] = "123456789";

    reverse(str);
    cout << str << endl;

    reverse(str1);
    cout << str1 << endl;
    return 0;
}
