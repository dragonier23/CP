#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int left, right;
    cin >> left >> right;

    if (left == 0 && right == 0){
        cout << "Not a moose";
    } else if (left != right){
        if (left > right){
            cout << "Odd " << left * 2;
        } else {
            cout << "Odd " << right * 2;
        }
    } else { 
        cout << "Even " << left * 2;
    }
    return 0;
}