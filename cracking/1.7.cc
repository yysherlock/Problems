#include <iostream>

using namespace std;

const int N = 4;

void rotate(int d[N][N]){

    for (int l = 0; l < N/2; ++l) {
        int first = l;
        int last = N - 1 - l;
        for ( int i=first; i<last; ++i){
            int offset = i - first;
            int top = d[first][i];
            d[first][i] = d[last-offset][first];
            d[last-offset][first] = d[last][last-offset];
            d[last][last-offset] = d[i][last];
            d[i][last] = top;
        }
    }

}

int main(){
    int a[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    rotate(a);
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }

    return 0;
}
