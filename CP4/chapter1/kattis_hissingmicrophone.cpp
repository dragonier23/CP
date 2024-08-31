#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  char* input = (char*) malloc(sizeof(char) * 30);
  scanf("%s", input);

  int n = 0, s = 0;
  while (input[n] != '\n'){
    if (input[n] != 's'){
      s = 0;
    }
    else {
      if (s == 1){
        printf("hiss");
        s += 1;
        break;
      }
      else {
        s += 1;
      }
    }
    n += 1;
  }
  if (s != 2){
    printf("no hiss");
  }
  return 0;
}
