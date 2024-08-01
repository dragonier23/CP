#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int n, curr, max, min;
    int count = 1;
    while (scanf("%d", &n) != EOF){
        max = -1000000;
        min = 1000000;
        
        while (n--){
            scanf("%d", &curr);
            if (curr > max) {
                max = curr;
            } 
            if (curr < min) {
                min = curr;
            }
        }

        printf("Case %d: %d %d %d \n", count, min, max, max - min);
        count += 1;
    }
    return 0;
}