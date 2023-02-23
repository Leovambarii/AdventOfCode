#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

void part_1() {
    std::vector<int> data_v;
    std::string input_line;
    std::ifstream input;
    long long int best_fuel_cost = 0;
    long long int fuel_cost = 0;

    input.open("input.txt");
    while(input >> input_line) {
        std::stringstream ss(input_line);
        int i;
        while(ss >> i) {
            data_v.push_back(i);
            if(ss.peek() == ',')
                ss.ignore();
        }
    }
    input.close();

    for(auto data : data_v) {
        std::cout<<data<<" ";
    }
    std::cout<<std::endl;
    int x=0;
    for(int i=0; i<data_v.size(); i++) {
        for(auto crab : data_v) {
            fuel_cost += abs(crab - i);
        }
        if(i==0)
            best_fuel_cost = fuel_cost;
        else if(fuel_cost < best_fuel_cost) {
            best_fuel_cost = fuel_cost;
            x = i;
        }
        std::cout<<fuel_cost<<" "<<i<<std::endl;
        fuel_cost=0;
    }
    std::cout<<"Best cost: "<<best_fuel_cost<<" For: "<<x<<std::endl;
}

void part_2() {
    std::vector<int> data_v;
    std::string input_line;
    std::ifstream input;
    long long int best_fuel_cost = 0;
    long long int fuel_cost = 0;

    input.open("input.txt");
    while(input >> input_line) {
        std::stringstream ss(input_line);
        int i;
        while(ss >> i) {
            data_v.push_back(i);
            if(ss.peek() == ',')
                ss.ignore();
        }
    }
    input.close();

    for(auto data : data_v) {
        std::cout<<data<<" ";
    }
    std::cout<<std::endl;
    int x = 0;
    int cost = 0;
    for(int i=0; i<data_v.size(); i++) {
        for(auto crab : data_v) {
            for(int j=0; j<abs(crab - i); j++) {
                cost += j+1;
            }
            fuel_cost += cost;
            cost = 0;
        }
        if(i==0)
            best_fuel_cost = fuel_cost;
        else if(fuel_cost < best_fuel_cost) {
            best_fuel_cost = fuel_cost;
            x = i;
        }
        std::cout<<fuel_cost<<" "<<i<<std::endl;
        fuel_cost = 0;
    }
    std::cout<<"\nBest cost: "<<best_fuel_cost<<" For: "<<x<<" position"<<std::endl;
}



int main() {
    part_2();
}