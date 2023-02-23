#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

// 8 = abcdefg
// 7 = acf
// 4 = bcdf
// 1 = cf

void sortString(std::string section) {
    std::sort(section.begin(), section.end());
}

bool checkForChar(std::string section, char x) {
    bool if_contain = false;
    for(int i=0; i<section.size(); i++) {
        if(section[i] = x)  {
            if_contain = true;
            break;
        }
    }
    return if_contain;
}

void part_1() {
    std::string section;
    std::vector<std::string> sections_v;
    std::ifstream input;

    input.open("input.txt");
    while(input >> section) {
        if(section.compare("|") != 0)
            sections_v.push_back(section);
    }
    input.close();

    std::cout<<sections_v.size()<<std::endl;
}

int main() {
    part_1();
}






