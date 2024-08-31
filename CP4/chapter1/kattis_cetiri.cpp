#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int a[3], diff1, diff2; 
  scanf("%d %d %d", &a[0], &a[1], &a[2]);
  sort(a, a+3);

  diff1 = a[1] - a[0];
  diff2 = a[2] - a[1];

  if (diff1 == diff2){
    printf("%d", a[2] + diff1);
  }
  else if (diff1 > diff2){
    printf("%d", a[0] + diff2);
  }
  else{
    printf("%d", a[1] + diff1);
  }
  return 0;
}
