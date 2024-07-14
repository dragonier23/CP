#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    string name;
    getline(cin, name);
    cout << "Thank you, " << name << ", and farewell!" << endl;
    //char name[50]; 
    //scanf("%[^\n]", name); // match until meeting a newline char
    //printf("Thank you, %s, and farewell!!", name);
    //return 0;
}