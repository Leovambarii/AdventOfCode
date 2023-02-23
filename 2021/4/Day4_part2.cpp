#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>

#define SIZE 5
#define NUMBER_OF_ARRAYS 3

using namespace std;

struct bingo_data {
    int column = 0;
    int row = 0;
};

int main() {
    fstream input;
    int value, steps_counter, last_value;
    string line;
    int Tab[SIZE][SIZE];
    int Tab_best[SIZE][SIZE];
    bingo_data Steps[2][SIZE] = {0};
    vector<int> v_numbers;
    vector<int> v_steps;

    input.open("input.txt", ios::in);
    if(input.is_open()) {
        getline(input, line);
        stringstream ss(line);
        for(int i; ss>> i;) {
            v_numbers.push_back(i);
            if(ss.peek() == ',')
                ss.ignore();
        }

        while(!input.eof()) {
            getline(input, line);
            for(int i=0; i<SIZE; i++) {
                for(int j=0; j<SIZE; j++) {
                    input>>value;
                    Tab[i][j] = value;
                }
            }
            steps_counter = 1;
            int found = 0;
            bool if_bingo = false;
            for(int number : v_numbers) {
                if(if_bingo == true)
                    break;
                for(int i=0; i<SIZE; i++) {
                    for(int j=0; j<SIZE; j++) {
                        if(number == Tab[i][j]) {
                            Steps[0][i].row++;
                            Steps[1][j].column++;
                            if(Steps[0][i].row == 5 || Steps[1][j].column == 5) {
                                v_steps.push_back(steps_counter);
                                if_bingo = true;
                                int it = *max_element(begin(v_steps), end(v_steps));
                                if(it == steps_counter){
                                    last_value = number;
                                    copy(&Tab[0][0], &Tab[0][0]+SIZE*SIZE, &Tab_best[0][0]);
                                }
                            }
                        }
                    }
                }
                steps_counter++;
            }
            memset(Tab,0,sizeof(Tab));
            memset(Steps,0,sizeof(Steps));
        }
    }

    input.close();

    for(int number : v_numbers) {
        if(number == last_value) {
            break;
        }
        for(int i=0; i<SIZE; i++) {
            for(int j=0; j<SIZE; j++) {
                if(number == Tab_best[i][j])
                    Tab_best[i][j] = 0;
            }
        }
    }

    int result = 0;
    for(int i=0; i<SIZE; i++) {
        for(int j=0; j<SIZE; j++) {
            cout<<Tab_best[i][j]<<" ";
            result += Tab_best[i][j];
        }
        cout<<endl;
    }

    cout<<"Result: "<<(result - last_value)*last_value<<endl;

}