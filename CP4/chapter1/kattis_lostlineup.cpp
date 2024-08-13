#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int n, d;
  scanf("%d", &n);
  int* output = (int*) malloc(sizeof(int) * (n));
  output[0] = 1;
  for (int i = 0; i < n-1; i++){
    scanf("%d", &d);
    output[d+1] = i+2;
  }
  for (int i = 0; i < n; i++){
    printf("%d ", output[i]);
  }
  return 0;
}
