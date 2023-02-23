#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int x=0,y=0,aim=0;
    string command;
    int value;
    string case_1 = "forward";
    string case_2 = "down";
    string case_3 = "up";

    fstream input;

    input.open("input.txt", ios::in);
    if(input.is_open()) {
        while(!input.eof()) {
            input>>command>>value;

            if(command == case_1) {
                x += value;
                y += aim*value;
            } else if(command == case_2) {
                aim += value;
            } else if(command == case_3) {
                aim -= value;
            }
        }
    }
        cout<<"("<<x<<","<<y<<")"<<endl;
        cout<<x*y<<endl;

    input.close();
}
