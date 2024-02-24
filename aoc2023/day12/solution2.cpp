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

typedef struct node {
    node* dot;
    node* hash;
    long long counter;
    long long temp; 
    bool end;
} node;

node* createDFA(vector<int> damagedList){
    node* tmp = (node*)malloc(sizeof(node));
    node* start = tmp, *next;
    for (int times = 0; times < 5; times++){
        for (int i = 0; i < damagedList.size(); i++){
            next = (node*)malloc(sizeof(node));
            tmp->dot = tmp;
            tmp->hash = next;
            tmp->counter = 0;
            tmp->temp = 0;
            tmp->end = false;
            tmp = next;
            for (int j = 0; j < (damagedList[i] - 1); j++){
                next = (node*)malloc(sizeof(node));
                tmp->dot = nullptr;
                tmp->hash = next;
                tmp->counter = 0;
                tmp->temp = 0;
                tmp->end = false;
                tmp = next; 
            }
            next = (node*)malloc(sizeof(node));
            tmp->dot = next; 
            tmp->hash = nullptr;
            tmp->counter = 0;
            tmp->temp = 0;
            tmp->end = false;
            tmp = next;
        }
    }
    //this is the end of the linked list
    tmp->dot = tmp;
    tmp->hash = nullptr; 
    tmp->counter = 0;
    tmp->temp = 0;
    tmp->end = true;
    return start;
}


long long countConfig(string config, vector<int> damagedList){
    node* start = createDFA(damagedList);
    node* curr = start;
    string config2 = config;
    for (int i = 0; i < 4; i++){
        config += ('?' + config2);
    }
    curr->counter = 1; 
    for (int i = 0; i < config.size(); i++){ 
        // we want to iterate through the whole line, then, go through the linked list, incrementing
        // if possible.
        curr = start;
        //while not at the end of the line;  THERE IS A PROBLEM HERE -> we increment more than we need to!!
        while (!(curr->end)){
            long long increment = curr->counter;
            curr->counter = 0;
            if (config[i] == '.' || config[i] == '?'){
                if ((curr->dot)){
                    curr->dot->temp += increment;
                }
            }
            if (config[i] == '#' || config[i] == '?'){
                if ((curr->hash)){
                    curr->hash->temp += increment;
                }
            }
            // we need to reassign it
            curr = (curr->hash) ? curr->hash : curr->dot;
        }
        //we need to do it for the last element too
        long long increment = curr->counter;
        curr->counter = 0;
        if (config[i] == '.' || config[i] == '?'){
            if ((curr->dot)){
                curr->dot->temp += increment;
            }
        }
        curr = start;
        while (!(curr->end)){
            curr->counter = curr->temp;
            curr->temp = 0;
            curr = (curr->hash) ? curr->hash : curr->dot;
        }
        curr->counter = curr->temp;
        curr->temp = 0;
    }
    // so we are done running through the list, now we need to sum the counter of the last 2 nodes
    // we will make curr hold the last one, and start hold the second last
    curr = start->hash;
    while (!(curr->end)){
        start = curr;
        curr = (curr->hash) ? curr->hash : curr->dot;
    }
    //cout << curr->counter << ' ' << start->counter << ' ' << endl;
    long long count = curr->counter + start->counter;
    return count;
}


int main() { 
    
    string line;
    ifstream readFile("problemstatement.txt"); //"test.txt"


    long long ans = 0;
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

        long long lineSolutions = countConfig(config, damagedList);
        ans += lineSolutions;

        cout << lineSolutions << endl;

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

