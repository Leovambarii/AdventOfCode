#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

#define file_name "input.txt"
#define days_number 256
#define new_fish_timer 8
#define fish_zero_timer -1
#define old_fish_timer 6

struct Fish {
    int timer = 0;
};

void part_1() {
    std::fstream input("input.txt");
    std::string line;
    std::vector<int> final_v;
    std::vector<Fish> lantern_fish;
    std::vector<Fish> temp;

    while(input >> line) {
        std::stringstream ss(line);
        int i;
        while(ss >> i) {
            final_v.push_back(i);
            if(ss.peek() == ',')
                ss.ignore();
        }
    }
    input.close();

    for(auto final : final_v) {
        Fish fish;
        fish.timer = final;
        lantern_fish.push_back(fish);
    }

    for(int i=0; i<days_number; i++) {
        std::cout<<"Day "<<i+1<<": ";
        for(auto fish : lantern_fish) {
            fish.timer--;
            if(fish.timer == fish_zero_timer) {
                Fish new_fish;
                new_fish.timer = new_fish_timer;
                temp.push_back(new_fish);
                fish.timer = old_fish_timer;
                temp.push_back(fish);
            } else {
                temp.push_back(fish);
            }
        }
        lantern_fish.clear();

        for(auto fish : temp)
            lantern_fish.push_back(fish);

        temp.clear();

        std::cout<<lantern_fish.size()<<std::endl;
    }
}

void part_2() {
    unsigned long long int lantern_fish_Count[7] = {};
    unsigned long long int baby_lantern_Count[7] = {};
    int lantern_fish_Day[7] = {0,1,2,3,4,5,6};
    int baby_lantern_Day[7] = {};
    int lantern_fish_Spawn[7] = {2,3,4,5,6,0,1};
    unsigned long long int total_fish_count = 0;

    std::string input_line;
    std::ifstream inputFile;
    inputFile.open("input.txt");
    inputFile >> input_line;
    inputFile.close();

	for (int i=0; i<input_line.length(); i+=2) {
        lantern_fish_Count[static_cast<int>(input_line[i])-48]++;
    }

    for(int i=0; i<days_number; i++) {
        for(int j=0; j<7; j++) {
            if(lantern_fish_Day[j] == 0) {
                    lantern_fish_Day[j] = old_fish_timer;
                    baby_lantern_Count[lantern_fish_Spawn[j]]+=lantern_fish_Count[j];
                    baby_lantern_Day[lantern_fish_Spawn[j]] = 2;
                } else
                    lantern_fish_Day[j]--;

            if (baby_lantern_Day[j] == 0) {
                lantern_fish_Count[j] += baby_lantern_Count[j];
                baby_lantern_Count[j] = 0;
            } else
                baby_lantern_Day[j]--;
        }
    }

    for (int i=0; i<7; i++) {
        total_fish_count += lantern_fish_Count[i] + baby_lantern_Count[i];
    }
    std::cout<<total_fish_count<<std::endl;
}

int main() {
    part_2();
}


using namespace std;

// void part_2() {
//     unsigned long long int lantern_fish_Count[7] = {};
//     unsigned long long int baby_lantern_Count[7] = {};
//     int lantern_fish_Day[7] = { 0,1,2,3,4,5,6 };
//     int baby_lantern_Day[7] = { 0,0,0,0,0,0,0 };
//     int lantern_fish_Spawn[7] = { 2,3,4,5,6,0,1 };
//     unsigned long long int totalFish = 0;

//     std::string inputData;

//     std::ifstream inputFile;
//     inputFile.open("input.txt");
//     inputFile >> inputData;
//     inputFile.close();

// 	for (int i = 0; i < inputData.length(); i += 2) {
//         lantern_fish_Count[static_cast<int>(inputData[i])-48]++;
//     }

//     for(int i=0; i<days_number; i++) {
//         for(int j=0; j<7; j++) {
//             if(lantern_fish_Day[j] == 0) {
//                     lantern_fish_Day[j] = old_fish_timer;
//                     baby_lantern_Count[lantern_fish_Spawn[j]]+=lantern_fish_Count[j];
//                     baby_lantern_Day[lantern_fish_Spawn[j]] = 2;
//                 } else
//                     lantern_fish_Day[j]--;

//             if (baby_lantern_Day[j] == 0) {
//                 lantern_fish_Count[j] += baby_lantern_Count[j];
//                 baby_lantern_Count[j] = 0;
//             } else
//                 baby_lantern_Day[j]--;
//         }
//     }

//     for (int i=0; i<7; i++) {
//         totalFish += lantern_fish_Count[i] + baby_lantern_Count[i];
//     }
//     std::cout<<totalFish<<std::endl;
// }
