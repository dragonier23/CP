#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

double eqn(int p, int a, int b, int c, int d, int input){
  return p * (sin((a * input) + b) + cos((c * input) + d) + 2);
}

int main() {
  int p, a, b, c, d, n;
  double curr, newdiff; 
  scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &d, &n);

  double diff = 0;
  double max = eqn(p, a, b, c, d, 1);

  for (int i = 2; i <= n; i++){
    curr = eqn(p, a, b, c, d, i);
    if (curr > max){
      max = curr;
      continue;
    }
    newdiff = max - curr;
    if (newdiff > diff){
      diff = newdiff;
    }
  }

  printf("%f", diff);

  return 0;
}
