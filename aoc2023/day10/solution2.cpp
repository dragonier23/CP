#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <numeric>
#include <set>

using namespace std;

vector<int> chooseNext(vector<int> curr, vector<int> prev, vector<vector<char>> pipeMap){
    int x = curr[0];
    int y = curr[1];
    char currSymbol = pipeMap[x][y];
    if (currSymbol == '-'){ if (prev[0] == x && prev[1] == y-1){ return {x, y+1}; } else { return{x, y-1}; } }
    if (currSymbol == '|'){if (prev[0] == x+1 && prev[1] == y){return {x-1, y};} else {return{x+1, y};}}
    if (currSymbol == '7'){if (prev[0] == x && prev[1] == y-1){return {x+1, y};} else {return{x, y-1};}}
    if (currSymbol == 'J'){if (prev[0] == x && prev[1] == y-1){return {x-1, y};} else {return{x, y-1};}}
    if (currSymbol == 'L'){if (prev[0] == x && prev[1] == y+1){return {x-1, y};} else {return{x, y+1};}}
    if (currSymbol == 'F'){if (prev[0] == x && prev[1] == y+1){return {x+1, y};} else {return{x, y+1};}}
    return {0, 0};    
}

vector<int> chooseFirst(vector<int> curr, vector<vector<char>> pipeMap){
    int x = curr[0], y = curr[1];
    if (pipeMap[x][y-1] == '-' || pipeMap[x][y-1] == 'F' || pipeMap[x][y-1] == 'L'){return {x, y-1};}
    if (pipeMap[x+1][y] == '|' || pipeMap[x+1][y] == 'J' || pipeMap[x+1][y] == 'L'){return {x+1, y};}
    if (pipeMap[x][y+1] == '-' || pipeMap[x][y+1] == 'J' || pipeMap[x][y+1] == '7'){return {x, y+1};}
    if (pipeMap[x-1][y] == '|' || pipeMap[x-1][y] == 'F' || pipeMap[x-1][y] == '7'){return {x-1, y};}
}

int findArea(vector<vector<int>> walls, int index){
    int sum = 0;
    for (int i = 1; i <= index; i++){
        sum += walls[i%index][0] * (walls[(i+1)%index][1] - walls[(i-1)%index][1]);
    }
    return sum/2;
}

int main() { //basically a djikstra's algo 
    
    string line, number;
    ifstream readFile("problemstatement.txt"); //"test3.txt"

    vector<vector<char>> pipeMap;
    int row = 0, col, sRow, sCol;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        col = 0;
        vector<char> pipeLine;
        for (char pipe: line){
            pipeLine.push_back(pipe);
            if (pipe == 'S'){
                sRow = row;
                sCol = col;
            }
            col++;
        } 
        pipeMap.push_back(pipeLine);
        row++;
    }


    //method 1: pick's theorem, A = i + b/2 - 1 or i = A - b/2 + 1 ( i.e. interior pt = area - index/2 + 1)
    // we first need to calculate the area of the polygon of sorts
    //we have a few methods, but most of them involve recording down the walls
    /*vector<vector<int>> walls;

    vector<int> curr = chooseFirst({sRow, sCol}, pipeMap);
    vector<int> prev = {sRow, sCol};
    walls.push_back(prev);

    int index = 1;
    while (!(curr[0] == sRow && curr[1] == sCol)){
        //walls.push_back(curr);
        walls.insert(curr);
        vector<int> tmp = curr;
        curr = chooseNext(curr, prev, pipeMap);
        prev = tmp;
        index++;
    }

    //cout << index;

    //pick's theorem here
    int area = findArea(walls, index);

    int interior = area - (index/2) + 1;
    cout << interior;*/

    // method 2: emitting rays for each thing
    vector<int> curr = chooseFirst({sRow, sCol}, pipeMap);
    vector<int> prev = {sRow, sCol};

    //we convert all the loop's pipes to be 'W' --> for us to check
    while (!(curr[0] == sRow && curr[1] == sCol)){
        //walls.push_back(curr);
        pipeMap[prev[0]][prev[1]] = (pipeMap[prev[0]][prev[1]] == 'L' || pipeMap[prev[0]][prev[1]] == '7') ? 'D' :'W';
        vector<int> tmp = curr;
        curr = chooseNext(curr, prev, pipeMap);
        prev = tmp;
    }
    pipeMap[prev[0]][prev[1]] = 'W';
    
    //USELESS: quadrants, top right and going counterclockwise, for choosing the direction of the rays
    //vector<vector<int>> quad = {{1, -1}, {1, 1}, {-1, 1}, {-1, -1},  };
    int internal = 0;
    for (int i = 0; i < row; i++){
        for (int j = 0; j < col; j++){
            int wallPassed = 0;
            if (pipeMap[i][j] == 'W' || pipeMap[i][j] == 'D'){
                continue;
            } //if we get here, the elementt is not a wall --> we sould find out how many times it cut the 
            for (int diagonalRow = i, diagonalCol = j; diagonalRow >= 0 && diagonalRow < row && diagonalCol >= 0 && diagonalCol < col; diagonalRow++, diagonalCol ++){
                if (pipeMap[diagonalRow][diagonalCol] == 'W'){
                    wallPassed++;
                }
            }
            if (wallPassed%2 == 1){
                internal++;
            }
            
            cout << i << j << wallPassed << endl; 
        }
    }

    cout << internal;
    return 0;
}

