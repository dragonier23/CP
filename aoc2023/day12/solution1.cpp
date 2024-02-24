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

int countConfig(string config, vector<int> damagedList){
    //so this will be a recursive function, that looks down the configuration, taking one step at a time
    // base case 1: if config is empty and the damaged list is also empty, it is valid
    if (config.empty()){
        //if the configuration is empty, the damagedList too must be empty for 1 correct config 
        return ((damagedList.empty() ? 1 : 0));
    }

    // base case 2: if the damaged List is empty, and the config no longer contains #, it should be valid
    if (damagedList.empty()) {
        return ((config.find('#') != std::string::npos) ? 0 : 1);
    }
 
    int dotCase = 0, hashCase = 0;
    if (config[0] == '?' || config[0] == '.'){
        //if the first letter is a dot, or if we treat it as a dot, we move to find the next one
        dotCase = countConfig(config.substr(1, (config.size()-1)), damagedList);
    }

    if (config[0] == '?' || config[0] == '#'){
        
        
        if (config.size() < damagedList[0]){ // if the remaining config cannot fit the damagedList, it is invalid
            return dotCase + hashCase;
        } 
        // if the first char is a #, we should check if it is valid. 
        for (int i = 0; i < damagedList[0]; i++){
            if (config[i] == '.'){
                return dotCase;
            }
        }
        if (config.size() == damagedList[0]){ // only if it isnt the last one
            return ((damagedList.size() == 1) ? dotCase + 1 : dotCase);            
        }
        if (config[damagedList[0]] == '#'){
            return dotCase;
        }
        // at this point, we are sure that the list is so far valid, so we conduct recursion. 
        vector<int> concat (damagedList.begin() + 1, damagedList.end());
        hashCase = countConfig(config.substr(damagedList[0] + 1, (config.size() - 1)), concat);
    }
    return dotCase + hashCase;
}


int main() { 
    
    string line;
    ifstream readFile("problemstatement.txt"); //"test.txt"


    int ans = 0;
    while (getline(readFile, line)){ 
        // for solution 1, we will try to iterate through all potential possibilities, killing the run off
        // if we know that it wont work 

        // we need to 1. split the line into the half configuration format, then the number of broken
        // springs in a line -> calculate the number of possibilities for each line 
        regex splitLine("\\S+"), splitDamaged("(\\d+)");
        smatch match;

        regex_search(line, match, splitLine);
        string config = match[0];
        line = match.suffix().str();

        regex_search(line, match, splitLine);
        string damaged = match[0].str();
        vector<int> damagedList;
        while (regex_search(damaged, match, splitDamaged)){
            damagedList.push_back(stoi(match[0]));
            damaged = match.suffix().str();
        }
        //so now we have a string containing the part-configuration, and the damaged list in a vector

        int lineSolutions = countConfig(config, damagedList);
        ans += lineSolutions;

        /*string substring = config.substr(damagedList[0] + 1, (config.size() - 1));
        cout << substring << endl;
        vector<int> concat (damagedList.begin() + 1, damagedList.end());
        for (auto x: concat){
            cout << x << ' ';
        }
        cout << endl;*/
    }
    cout << ans; 

    return 0;
}

