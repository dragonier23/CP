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

vector<int> chooseNext(vector<int> curr, vector<int> prev, vector<vector<char>> pipeMap){
    int x = curr[0];
    int y = curr[1];
    char currSymbol = pipeMap[x][y];
    if (currSymbol == '-'){
        if (prev[0] == x && prev[1] == y-1){
            return {x, y+1};
        } else {
            return{x, y-1};
        }
    }
    if (currSymbol == '|'){
        if (prev[0] == x+1 && prev[1] == y){
            return {x-1, y};
        } else {
            return{x+1, y};
        }
    }
    if (currSymbol == '7'){
        if (prev[0] == x && prev[1] == y-1){
            return {x+1, y};
        } else {
            return{x, y-1};
        }
    }
    if (currSymbol == 'J'){
        if (prev[0] == x && prev[1] == y-1){
            return {x-1, y};
        } else {
            return{x, y-1};
        }
    }
    if (currSymbol == 'L'){
        if (prev[0] == x && prev[1] == y+1){
            return {x-1, y};
        } else {
            return{x, y+1};
        }
    }
    if (currSymbol == 'F'){
        if (prev[0] == x && prev[1] == y+1){
            return {x+1, y};
        } else {
            return{x, y+1};
        }
    }
    return {0, 0};    
}

vector<int> chooseFirst(vector<int> curr, vector<vector<char>> pipeMap){
    int x = curr[0], y = curr[1];
    if (pipeMap[x][y-1] == '-' || pipeMap[x][y-1] == 'F' || pipeMap[x][y-1] == 'L'){
        return {x, y-1};
    }
    if (pipeMap[x+1][y] == '|' || pipeMap[x+1][y] == 'J' || pipeMap[x+1][y] == 'L'){
        return {x+1, y};
    }
    if (pipeMap[x][y+1] == '-' || pipeMap[x][y+1] == 'J' || pipeMap[x][y+1] == '7'){
        return {x, y+1};
    }
    if (pipeMap[x-1][y] == '|' || pipeMap[x-1][y] == 'F' || pipeMap[x-1][y] == '7'){
        return {x-1, y};
    }
}

int main() { //basically a djikstra's algo 
    
    string line, number;
    ifstream readFile("problemstatement.txt"); //"test2.txt"

    vector<vector<char>> pipeMap;
    int row = 0, sRow, sCol;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        int col = 0;
        vector<char> pipeLine;
        for (char pipe: line){
            pipeLine.push_back(pipe);
            if (pipe == 'S'){
                sRow = row;
                sCol = col;
                //cout << sRow << endl << sCol << endl;
            }
            col++;
        } 
        pipeMap.push_back(pipeLine);
        row++;
    }
    vector<int> curr = chooseFirst({sRow, sCol}, pipeMap);
    vector<int> prev = {sRow, sCol};
    int index = 1;
    while (!(curr[0] == sRow && curr[1] == sCol)){
        vector<int> tmp = curr;
        curr = chooseNext(curr, prev, pipeMap);
        prev = tmp;
        index++;
    }

    cout << index;
    return 0;
}

