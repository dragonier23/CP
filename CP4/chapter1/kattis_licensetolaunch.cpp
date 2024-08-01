#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int n, curr, min, day;
  min = 1000000000;
  scanf("%d", &n);
  for (int i = 0; i < n; i++){
    scanf("%d", &curr);
    if (curr < min){
      min = curr;
      day = i;
    }
  }
  printf("%d", day);
  return 0;
}
