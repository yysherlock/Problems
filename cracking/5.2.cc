#include <iostream>
using std::cout;
using std::endl;

#include <vector>

namespace Solution1{ // my first solution

    struct DoubleBinaryRep {
        bool success = true;
        std::vector<int> integral;
        std::vector<int> fractional;

    };

    std::ostream& operator<<(std::ostream &os, const DoubleBinaryRep& obj) {
    //    os << "integral: ";
        int len = obj.integral.size();
        if (!len) os << "0";

        for (int i=len-1; i>=0; i--){
            os << obj.integral[i];
        }
        os << ".";
    //    os << endl;
    //    os << "fractional: 0." ;
        for (auto x : obj.fractional){
            os << x;
        }

        return os;
    }

    bool int2binary(int val, std::vector<int> &v){ // do not consider sign
        int len = 0;
        while (val) {
            if (len > 32) return false;
            v.push_back(val%2);
            ++len;
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
            ++len;
            v.push_back(bit);
            val = tmp - bit;
        }
        return true;
    }

    DoubleBinaryRep decimal2binary(double val){
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

}

#include <cstdlib>

namespace Solution2{ // solution learned from others
    std::string print_binary(std::string val){
        int pos = val.find('.', 0);
    //    cout << "pos:" << pos << endl; //
        /* previous: atoi
        int intpart = std::atoi(val.substr(0, pos).c_str());
        double decpart = std::atof(val.substr(pos).c_str());
        */
        /* C++11 NEW: stoi */
        int intpart = std::stoi(val.substr(0, pos));
        double decpart = std::stof(val.substr(pos));
    //    cout << "intpart: " << intpart << " " << "decpart: " << decpart << endl;

        std::string intstr = "", decstr = "";
        while (intpart > 0){
            if (intpart & 1) intstr = "1" + intstr;
            else intstr = "0" + intstr;
            intpart >>= 1; // alternative: intpart /= 2;
        }
        while (decpart > 0) {
            if (decstr.length() > 32) return "ERROR";
            decpart *= 2;
            if (decpart >= 1) {
                decstr += "1";
                decpart -= 1;
            }
            else decstr += "0";
        }
        return intstr + "." + decstr;
    }
}

using Solution1::DoubleBinaryRep;
using Solution1::decimal2binary;

using Solution2::print_binary;

int main(){
    double x = 0.25;
    double y = 8.25;
    // Solution1
    DoubleBinaryRep re = decimal2binary(y);
    if (re.success) cout << re << endl;
    else cout << "ERROR" << endl;

    // Solution2
    cout << print_binary("8.25") << endl;

}
