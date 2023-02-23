#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>

#define BITS_NUMBER 12

using namespace std;

inline int to_int(string binary) {
    return bitset<BITS_NUMBER>(binary).to_ulong();
}

struct data {
    unsigned one_counter = 0;
    unsigned zero_counter = 0;
};

bool f(vector<string> v, int bit) {
    data counter;
    for(auto str : v) {
        if(str.at(bit) == '1')
            counter.one_counter++;
        else
            counter.zero_counter++;
    }
    bit++;
    return counter.one_counter >= counter.zero_counter;
}

int get_number(vector<string> v, bool oxygen) {
    vector<string> temp;
    for(int i=0; i<BITS_NUMBER; i++) {
        bool erase_zero = f(v, i);
        if(!oxygen) erase_zero = !erase_zero;
        for(auto str : v) {
            if(erase_zero) {
                if(str.at(i) == '1')
                    temp.push_back(str);
            } else {
                if(str.at(i) == '0')
                    temp.push_back(str);
            }
        }
        v = temp;
        temp.clear();
        if(v.size() == 1)
            break;
    }
    return to_int(v.at(0));
}

int main() {
    string binary;
    bool erase_zero = false;
    data Tab[BITS_NUMBER];
    int bit=0;
    vector<string> raport;
    fstream input;
    input.open("input.txt", ios::in);

    while(input >> binary)
        raport.push_back(binary);

    int oxygen = get_number(raport, true);
    int CO2 = get_number(raport, false);

    cout<<oxygen<<" "<<CO2<<endl<<oxygen*CO2<<endl;

    input.close();
}