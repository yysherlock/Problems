#include <iostream>
using std::cout;
using std::endl;

#include <vector>

struct DoubleBinaryRep {
    bool success = true;
    std::vector<int> integral;
    std::vector<int> fractional;

};

std::ostream& operator<<(std::ostream &os, const DoubleBinaryRep& obj){
    os << "integral: ";
    if (!obj.integral.size()) cout << "0";
    for (auto x : obj.integral){
        os << x;
    }
    os << endl;
    os << "fractional: 0." ;
    for (auto x : obj.fractional){
        os << x;
    }
    //os << endl;
    return os;
}

bool int2binary(int val, std::vector<int> &v){ // do not consider sign
    int len = 0;
    while (val) {
        if (len > 32) return false;
        v.push_back(val%2);
        val /= 2;
    }
    return true;
}

bool frac2binary(double val, std::vector<int> &v){ // do not consider sign

    int len = 0;
    double epsilon = 1e-30;
    while (val >= epsilon) {
        if (len > 32) return false;
        double tmp = val*2;
        int bit = int(tmp);
        v.push_back(bit);
        val = tmp - bit;
    }
    return true;
}

DoubleBinaryRep decimal2binary(double val) {
    int integral = val;
    double fractional = val - integral;

    std::vector<int> inte;
    std::vector<int> fract;

    DoubleBinaryRep re;
    bool intConv = int2binary(integral, inte);
    re.integral = inte;
    bool fractConv = frac2binary(fractional, fract);
    re.fractional = fract;
    re.success = intConv && fractConv;
    return re;
}

int main(){
    double x = 0.25;
    DoubleBinaryRep re = decimal2binary(x);
    if (re.success) cout << re << endl;
    else cout << "ERROR" << endl;
}
