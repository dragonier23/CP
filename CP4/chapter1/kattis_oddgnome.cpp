#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int n, g, curr, prev;
  scanf("%d", &n);
  for (int i = 0; i < n; i++){
    scanf("%d", &g);
    scanf("%d", &prev);
    for (int index = 1; index < g; index++){
      scanf("%d", &curr);
      if (curr != prev + 1){
        printf("%d\n", index + 1);
        for (int tmp = index + 1; tmp < g; tmp++){
          scanf("%d", &prev);
        }
        break;
      }
      prev = curr;
    }
  }
  return 0;
}
