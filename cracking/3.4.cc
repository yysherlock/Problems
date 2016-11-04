#include <iostream>
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
    
}
int main(){
    hanoi(3, 'A', 'B', 'C');
    return 0;
}
