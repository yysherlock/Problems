#include <iostream>
using std::cout;
using std::endl;

#include <vector>

typedef unsigned char byte;

namespace Solution1{ // my first solution

    void show_screen(byte screen[]){
        //cout << sizeof(screen) << " " << sizeof(byte);
        int len = sizeof(screen)/sizeof(byte);
        cout << "len: " << len << endl;
        //cout <<  "len: " << len;
        for (int i=0; i<len; ++i){
            for (int pos=0; pos < 8; ++pos)
                if (screen[i] & (byte)(1<<pos)) cout << "1";
                else cout << "0";
            cout << " ";
        }
        cout << endl;
    }
    void print_byte(byte b){
        for (int pos=0; pos < 8; ++pos)
            if (b & (1<<pos)) cout << "1";
            else cout << "0";
    }

    bool drawHorizontalLine(byte screen[], int width, int x1, int x2, int y){
        cout << "before: ";
        show_screen(screen);
        int height = sizeof(screen)/sizeof(byte) * 8 / width ;
        if (y > height || x1 > width || x2 > width) return false;
        else {
            int start_idx = y * width/8 + x1/8;
            x1 %= 8;
            //int start_mask = (1 << x1) - 1;
            byte start_mask = ((byte)(0xFF)) << x1;
        /*    cout << "sm: ";
            print_byte(0xFF >> 3);
            cout << endl; */

            screen[start_idx] |= start_mask;
            int end_idx = y * width/8 + x2/8;
            x2 %= 8;
            //int end_mask = ~( (1 << (8-x2)) - 1 );
            byte end_mask = ((byte)(0xFF)) >> (8-(x2+1));
            screen[end_idx] |= end_mask;
            //int mask = (1<<8) - 1;
            byte mask = 0xFF; // smarter than (1<<8) - 1
            for (int idx=start_idx+1; idx < end_idx; ++idx){
                screen[idx] |= mask;
            }
        }

        cout << "after: ";
        show_screen(screen);
        return true;
    }

}

//using Solution1::drawHorizontalLine;

int main(){
    byte screen[] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
    Solution1::drawHorizontalLine(screen, 16, 4, 10, 1);
    return 0;
}
