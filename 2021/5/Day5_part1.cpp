#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

#define file_name "input.txt"
#define SIZE 1000

class Diagram {
    public:
        int Tab[SIZE][SIZE] = {};

    int find_over_2() {
        int counter = 0;
        for(int i = 0; i<SIZE; i++) {
            for(int j = 0; j<SIZE; j++) {
                if(Tab[i][j] >= 2)
                    counter++;
            }
        }
        return counter;
    }

    void display() {
        for(int i = 0; i<SIZE; i++) {
            for(int j = 0; j<SIZE; j++) {
                std::cout << Tab[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};

void first()
{
    std::fstream in(file_name);
    std::string line;
    std::vector<std::string> lines, final_v;
    Diagram diagram;

    while(in >> line)
        lines.push_back(line);

    lines.erase(std::remove(lines.begin(), lines.end(), "->"), lines.end());

    for(auto l : lines) {
        std::stringstream s1(l);
        while(s1.good()) {
            std::string substr;
            std::getline(s1, substr, ',');
            final_v.push_back(substr);
        }
    }

    int x1,x2,y1,y2;
    for(int i = 0; i<final_v.size(); i+=4) {
        x1 = atoi(final_v.at(i).c_str());
        y1 = atoi(final_v.at(i+1).c_str());
        x2 = atoi(final_v.at(i+2).c_str());
        y2 = atoi(final_v.at(i+3).c_str());

        if(x1 > x2) std::swap(x1,x2);
        if(y1 > y2) std::swap(y1,y2);

        if(x1 == x2) {
            for(int i = y1; i<=y2; i++)
                diagram.Tab[i][x1]++;
        } else if(y1 == y2) {
            for(int i = x1; i<=x2; i++)
                diagram.Tab[y1][i]++;
            }
    }
    diagram.display();
    std::cout << diagram.find_over_2() << std::endl;
}

int main()
{
    first();
}