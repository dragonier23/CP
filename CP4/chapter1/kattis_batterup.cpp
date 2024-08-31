#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int n, bases;
  scanf("%d", &n);
  
  float count = 0, total = 0;
  for (int i = 0; i < n; i++){
    scanf("%d ", &bases);
    if (bases == -1){
      continue;
    }
    total += bases;
    count++;
  }
  float ans = total / count;
  printf("%f", ans);
  return 0;
}
