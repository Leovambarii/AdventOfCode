#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int counter = 0;

    fstream input;
    fstream output;

    input.open("input.txt", ios::in);
    output.open("output.txt", ios::out);

    if(input.is_open()) {
        string depth1, depth2;

        getline(input, depth1);
        int depth1_val = stoi(depth1);

        while(getline(input, depth2)) {
            int depth2_val = stoi(depth2);
            if(depth2_val > depth1_val) {
                counter++;
                output<<depth2<<" increased"<<std::endl;
            } else {
                output<<depth2<<std::endl;
            }
            depth1_val = depth2_val;
        }
    }
    cout<<counter<<endl;

    input.close();
    output.close();
}