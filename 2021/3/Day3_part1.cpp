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

int main() {
    string binary;
    bool erase_zero = false;
    data Tab[BITS_NUMBER];
    int bit=0;
    vector<string> raport;
    fstream input;
    input.open("input.txt", ios::in);

    while(input >> binary) {
        for(int i=0; i<binary.length(); i++) {
            if(binary.at(i) == '1')
                Tab[i].one_counter++;
            else
                Tab[i].zero_counter++;
        }
    }
    string gamma = "", epsilon = "";
    for(int i=0; i<BITS_NUMBER; i++) {
        gamma += Tab[i].one_counter > Tab[i].zero_counter ? '1' : '0';
        epsilon += Tab[i].one_counter < Tab[i].zero_counter ? '1' : '0';
    }
    cout<<to_int(gamma)*to_int(epsilon)<<endl;

    input.close();
}