#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <numeric>

using namespace std;

bool checkZero(vector<int> line){
    for (int entry: line){
        if (entry != 0){
            return false;
        }
    }
    return true;
}

int main() {
    
    string line, number;
    ifstream readFile("problemstatement.txt"); //"test.txt"

    long long ans = 0;
    vector<vector<int>> split;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        split.clear();
        regex pattern ("-?\\d+");
        smatch m;

        vector<int> appendLine; // geg out each line of the problem, now we try to solve
        while (regex_search(line, m, pattern)){
            appendLine.push_back(stoi(m[0]));
            line = m.suffix().str();
        }

        while (!checkZero(appendLine)){
            split.push_back(appendLine);
            for (auto element: appendLine){
                cout << element << endl;
            }
            appendLine.clear();
            for (int i = 0; i < (split.back().size() - 1); i++){
                appendLine.push_back((split.back()[i+1] - split.back()[i])); 
            }
        }

        //so now we reached the point that all elements in the last row are 0s, so now we add
        long long nextNum = 0;
        for (int j = (split.size() - 1); j >= 0; j--){
            nextNum = split[j][0] - nextNum;
        }
        cout << nextNum << endl;
        ans += nextNum;
    }

    cout << ans;
    return 0;
}

