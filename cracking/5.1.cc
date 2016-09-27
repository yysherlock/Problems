#include <iostream>
using std::cout;
using std::endl;

#include <vector>

int insertNum(int N, int M, int i, int j){
    for (int k=i; k<=j; k++){
        int kthM = ((1 << (k-i)) & M) != 0;     // get kth bit of M
	    N = (N & (~( 1 << k ))) | (kthM << k); // set bit
        //cout << k << " " << kthM << " "<< N << endl;
    }
    return N;
}

int iOneBitsSuffix(int i){
    return (1<<i) - 1; // 0..01..1, iS 1 suffix
    /* Alternative
    return ~ ( (~0) << i );
    */
}

int iZeroBitsSuffix(int i){
    return ~0 << i ; // 1..10..0, iS 0 suffix
}

int update_bits(int N, int M, int i, int j){
    return ( N & (~((~0) << i)) ) | (M << i)  | (N & ((~0) << (j+1)));
}

void  print_binary(int n) {
    std::vector<int> v;
    int len = 8 * sizeof(int);
    int mask = 1;
    while (len--){
        if(n & mask) v.push_back(1);
        else v.push_back(0);
        mask <<= 1;
    }
    while (!v.empty()){
        cout << v.back();
        v.pop_back();
    }
    cout << endl;
}

int main(){
    int n = 1<<10, m = 19;
    cout << insertNum(n,m,2,6) << endl; // 1100
    cout << update_bits(n,m,2,6) << endl; // 1100

    int max = ~0;
    cout << max << endl;
    print_binary(~((~0) << 7));

    print_binary(19);
    print_binary(max); // 11...1, 32 1S

    print_binary(iZeroBitsSuffix(2));

}
