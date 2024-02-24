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

int main() { //basically a djikstra's algo 
    
    string line;
    ifstream readFile("problemstatement.txt"); //"test.txt"

    // for this solution, we will 
    // 1. convert it to an array of char (actually not necessary)
    // 2. keep track of the rows and column without galaxies 
    // 3. keep track of the location of the galaxies

    //vector<vector<char>> skyMap;
    vector<int> rowCount, colCount;
    vector<vector<int>> galaxyLoc;

    // to determine no of columns, we need to do the first row differently
    getline(readFile, line);
    rowCount.push_back(0);
    for (int col = 0; col < line.size(); col++){
        if (line[col] == '#'){ // if it is a galaxy, add the coordinates to our list + indicate that column has 1 galaxy
            vector<int> galaxy = {0, col};
            galaxyLoc.push_back(galaxy);
            colCount.push_back(1);
            rowCount.back()++;
        } else { //just indicate the column currently has no galaxies
            colCount.push_back(0);
        }
    }

    // now we need to settle for the other rows - we also need to keep track of the row number
    int row = 1;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        rowCount.push_back(0);
        for (int col = 0; col < line.size(); col++){
            if (line[col] == '#'){ // if it is a galaxy, add the coordinates to our list + indicate that column has 1 galaxy
                vector<int> galaxy = {row, col};
                galaxyLoc.push_back(galaxy);
                colCount[col]++;
                rowCount.back()++;
            } 
        }
        row++;
    }

    // so now we just need to find the shortest distance between each galaxy
    unsigned long long ans = 0;
    int galaxyCount = galaxyLoc.size();
    for (int i = 0; i < galaxyCount; i++){
        for (int j = i + 1; j < galaxyCount; j++){
            int galaxy1X = galaxyLoc[i][1], galaxy1Y = galaxyLoc[i][0],
                galaxy2X = galaxyLoc[j][1], galaxy2Y = galaxyLoc[j][0];
            if (galaxy1X > galaxy2X){ //lets make sure that coordinate no2 is always larger
                int tmp = galaxy2X;
                galaxy2X = galaxy1X;
                galaxy1X = tmp;
            }
            if (galaxy1Y > galaxy2Y){
                int tmp = galaxy2Y;
                galaxy2Y = galaxy1Y;
                galaxy1Y = tmp;
            }
            unsigned long xDist = galaxy2X - galaxy1X, yDist = galaxy2Y - galaxy1Y;
            for (int x = galaxy1X; x < galaxy2X; x++){
                if (!colCount[x]){
                    xDist += 999999;
                }
            }
            for (int y = galaxy1Y; y < galaxy2Y; y++){
                if (!rowCount[y]){
                    yDist += 999999;
                }
            }
            ans += (xDist + yDist);
        }
    }

    cout << ans;

    return 0;
}

