#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    long p, q;
    while (scanf("%ld %ld", &p, &q) == 2){
        printf("%ld\n", abs(p - q));
    }
    return 0;
}