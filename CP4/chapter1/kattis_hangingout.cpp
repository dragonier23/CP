#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <cstring>

using namespace std;

int main() {
  int L, x, p;
  char* type = (char*) malloc(sizeof(char) * 6);

  scanf("%d %d", &L, &x);
  int curr = 0, ans = 0;
  for (int i = 0; i < x; i++){
    scanf("%s %d", type, &p);
    if (!strcmp(type, "enter")){
      if (curr + p > L){
        ans++;
      } else {
        curr += p;
      }
    } else {
      curr -= p;
    }
  }
  printf("%d", ans);

  return 0;
}
