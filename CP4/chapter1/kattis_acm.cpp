#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>
#include <cstring>

using namespace std;

int main() {
  int n, mnumber;
  char m, result[6];
  int* count = (int*) malloc(sizeof(int) * 26);

  int timeanswer = 0;
  int solvedanswer = 0;
  
  while (scanf("%d ", &n), (n != -1)){
    scanf("%c %s", &m, result);
    mnumber = m - 65;
    if (count[mnumber] == -1){
      continue;
    } 
    if (!strcmp("right", result)){
      timeanswer += n + (count[mnumber] * 20);
      count[mnumber] = -1;
      solvedanswer += 1;
    }
    else {
      count[mnumber] += 1;
    }
  }
  printf("%d %d\n", solvedanswer, timeanswer);
  return 0;
}
