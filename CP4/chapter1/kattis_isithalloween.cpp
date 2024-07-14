#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    string input;
    int date;

    cin >> input >> date;
    if ((input == "OCT" && date == 31) || (input == "DEC" && date == 25)){
        cout << "yup";
    } else {
        cout << "nope";
    }

    return 0;
}