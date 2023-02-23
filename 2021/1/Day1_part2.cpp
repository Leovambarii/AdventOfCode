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
        string depth1, depth2, depth3, depth;

        getline(input, depth1);
        getline(input, depth2);
        getline(input, depth3);

        int depth1_val = stoi(depth1);
        int depth2_val = stoi(depth2);
        int depth3_val = stoi(depth3);
        int sum = depth1_val+depth2_val+depth3_val;
        output<<sum<<" (N/A - no previous sum)"<<endl;

        while(getline(input, depth)) {
            int depth_val = stoi(depth);

            int sum_2 = depth_val+depth2_val+depth3_val;

            if(sum_2 > sum) {
                output<<sum_2<<" (increased)"<<endl;
                counter++;
            } else {
                output<<sum_2<<" (decreased)"<<endl;
            }

            depth2_val = depth3_val;
            depth3_val = depth_val;
            sum = sum_2;
        }
    }
    cout<<counter<<endl;

    input.close();
    output.close();
}