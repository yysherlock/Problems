#include <iostream>
using namespace std;

const int M = 3;
const int N = 4;

void setZeros(int d[M][N]){
    bool row[M];
    memset(row, false, M);
    bool col[N];
    memset(col, false, N);

    for(int i=0; i < M; ++i){
        for(int j=0; j < N; ++j){
            if (d[i][j] == 0) {
                row[i] = true;
                col[j] = true;
                break;
            }
        }
    }

    for(int i=0; i < M; ++i){
        for(int j=0; j < N; ++j){
            if(row[i] || col[j]) d[i][j] = 0;
        }
    }

}

int main(){

    int a[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 0, 8},
        {9, 0, 0, 12},
        {13, 14, 15, 16}
    };
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    setZeros(a);
    for(int i=0; i<4; ++i){
        for(int j=0; j<4; ++j)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }

    return 0;
}
