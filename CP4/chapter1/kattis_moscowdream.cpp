#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int a, b, c, n;
    scanf("%d %d %d %d", &a, &b, &c, &n);
    if (a < 1 || b < 1 || c < 1 || a + b + c < n || n < 3){
        printf("NO");
    }
    else {
        printf("YES");
    }
    return 0;
}