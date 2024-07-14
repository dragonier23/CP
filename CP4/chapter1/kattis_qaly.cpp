#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    float ans = 0;
    for (int i = 0; i < n; i++){
        float q, y;
        scanf("%f %f", &q, &y);
        ans += q * y;
    }
    printf("%f", ans);
}