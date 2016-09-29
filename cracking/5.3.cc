#include <iostream>
using std::cout;
using std::endl;

#include <vector>

void print_int(int b){
    for (int pos=31; pos >= 0; pos--)
        if (b & (1<<pos)) cout << "1";
        else cout << "0";
}

int getNext(int n){
    // "01" -> "10"
    int pos = 0, bit = 0;

    while ( !bit && pos < 32){
        bit = n & (1<<pos);
        ++pos;
    }
    --pos;
    int c1 = 0;
    while (bit && pos < 32) {
        c1 += 1;
        n &= ~(1<<pos); // clear bit
        ++pos;
        bit = n & (1<<pos);
    }
    // set bit
    n |= (1<<pos);

    // rerange c1-1 1S to lowest bits
    int mask = (1<<(c1-1)) - 1 ;
    n |= mask;
    /*
    cout << "mask: ";
    print_int(mask);
    cout << endl; */
    return n;
}

int getPrev(int n){
    // "10" -> "01"
    int pos = 0, bit = 1 & n;
    int c1 = 0;
    while (bit && pos < 32){
        c1 += 1;
        n &= ~(1<<pos);  // clear bit
        ++pos;
        bit = n & (1<<pos);
    }
    int c0 = 0;
    while(!bit && pos < 32){
        c0 += 1;
        ++pos;
        bit = n & (1<<pos);
    }
    //int c0 = pos-c1;
    // 1 -> 0
    n &= ~(1<<pos);
    int mask1 = ~(1<<(c0-1) - 1);
    int mask2 = (1<<pos) - 1;
    int mask = mask1 & mask2;
    /*cout << "mask: ";
    print_int(mask); cout << endl; */
    n |= mask;

    return n;
}

void neighborEqual1s(int n){
    print_int(getNext(n));
    cout << endl;
    print_int(getPrev(n));
    cout << endl;
}

int main(){
    print_int(22); cout << endl;
    neighborEqual1s(22);
    cout << endl;
    print_int(13948); cout << endl;
    neighborEqual1s(13948);
    return 0;
}
