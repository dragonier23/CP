#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int x, y;
    while (scanf("%d %d", &x, &y), (x || y)){
        if (x + y == 13){
            cout << "Never speak again.\n";
        } else if (x > y){
            cout << "To The convention.\n";
        } else if (x == y) {
            cout << "Undecided.\n";
        } else {
            cout << "Left beehind.\n";
        }
    }
    return 0;
}