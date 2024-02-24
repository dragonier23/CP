#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;

const string START = "AAA";
const string END = "ZZZ";

int main() {
    
    string line;
    ifstream readFile("test2.txt"); //"problemstatement.txt"

    // extract the sequence into a vector, where 0 rep left and 1 rep right
    getline(readFile, line);
    vector<int> sequence;
    for (char letter: line){
        if (letter == 'L'){
            sequence.push_back(0);
        }
        else{
            sequence.push_back(1);
        }
    }

    // ignore the empty line
    getline(readFile, line);

    //read each line of the file, adding it to an hashtable with the next steps
    unordered_map<string, vector<string>> directionMap;
    while (getline(readFile, line)){ //this line reads each line, and stores it in the variable line
        smatch m;
        regex pattern ("[A-Z]+");

        vector<string> mappings;
        while(regex_search(line, m, pattern)){
            mappings.push_back(m[0]);
            line = m.suffix().str();
        }

        directionMap[mappings[0]] = {mappings[1], mappings[2]};
    }
    
    string currString = START;
    int index = 0;
    int seqSize = sequence.size();
    while (currString != END){
        if (sequence[(index%seqSize)]){ //if the sequence returns a 1, which is true, we find the right side
            currString = directionMap[currString][1];
        } else {
            currString = directionMap[currString][0];
        }
        index++;
    }

    cout << index;

    return 0;
}

