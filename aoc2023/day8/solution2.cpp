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


int main() {
    
    string line;
    ifstream readFile("problemstatement.txt"); //"test3.txt"

    vector<string> START;

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
        regex pattern ("[A-Z0-9]+");

        vector<string> mappings;
        while(regex_search(line, m, pattern)){
            mappings.push_back(m[0]);
            line = m.suffix().str();
        }

        if (mappings[0][2] == 'A'){
            START.push_back(mappings[0]);
            //cout << mappings[0] << endl;
        }
        directionMap[mappings[0]] = {mappings[1], mappings[2]};
    }
    
    unsigned long long ans = 1;
    int startSize = START.size();
    int seqSize = sequence.size();
    for (int i = 0; i < startSize; i++){
        int index = 0;
        while (START[i][2] != 'Z'){
            if (sequence[(index%seqSize)]){
                START[i] = directionMap[START[i]][1];
            } else {
                START[i] = directionMap[START[i]][0];
            }
            index++;
        }
        START[i] = index;
        cout << index << endl;
        ans = lcm(index, ans);
        cout << ans << endl;
    }

    cout << ans;
    return 0;
}

