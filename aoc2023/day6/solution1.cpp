#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int bounds(int time, int dist){
    float flowerBound = ((time) - sqrt(pow(time, 2) - 4*(dist))) / 2;
    float fupperBound = ((time) + sqrt(pow(time, 2) - 4*(dist))) / 2;
    int lowerBound = floor(flowerBound) + 1;
    int upperBound = ceil(fupperBound) - 1;
    int ways = upperBound - lowerBound + 1;
    return ways;
}


int main() {
    string line;
    ifstream readFile("problemstatement.txt"); //"text.txt"
    
    regex pattern("\\d+");
    smatch matches;

    getline(readFile, line); // read first line    
    vector<int> time;
    while (regex_search(line, matches, pattern)){
        for (auto& match: matches){
            time.push_back(stoi(match.str()));
        }
        line = matches.suffix().str();
    }


    getline(readFile, line);
    vector<int> minDist;
    while (regex_search(line, matches, pattern)){
        for (auto& match: matches){
            minDist.push_back(stoi(match.str()));
        }
        line = matches.suffix().str();
    }


    int count = 1;
    for (int i = 0; i < time.size(); i++){
        int val = bounds(time[i], minDist[i]);
        cout << val << endl;
        count *= val;
    }
    cout << count;
    return 0;
}

