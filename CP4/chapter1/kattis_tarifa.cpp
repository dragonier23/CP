#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int x, n;
    scanf("%d \n %d ", &x, &n);
    int ans = 0;

    for (int i = 0; i < n; i++){
        int p;
        scanf("%d", &p);
        ans += x - p;
    }
    printf("%d", ans + x);
}
