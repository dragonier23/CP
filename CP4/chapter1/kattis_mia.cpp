#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int s0, s1, r0, r1;
  while (scanf("%d %d %d %d", &s0, &s1, &r0, &r1), (s1 || s0 || r0 || r1)){

    if (((s1 == 1 && s0 == 2) || (s1 == 2 && s0 == 1)) && ((r1 == 1 && r0 == 2) || (r1 == 2 && r0 == 1))){
      printf("Tie.\n");
    } else if ((s1 == 1 && s0 == 2) || (s1 == 2 && s0 == 1)){
      printf("Player 1 wins.\n");
    } else if ((r1 == 1 && r0 == 2) || (r1 == 2 && r0 == 1)){
      printf("Player 2 wins.\n");
    } 

    else if (s1 == s0 && r1 == r0){
      if (s1 == r0){
        printf("Tie.\n");
      } else {
        printf("Player %d wins.\n", (r1 > s1) ? 2 : 1);
      }
    } else if (s1 == s0) {
      printf("Player 1 wins.\n");
    } else if (r1 == r0) {
      printf("Player 2 wins.\n");
    } 

    else {
      if (max(s1, s0) == max(r1, r0)){
        if (min(s1, s0) == min(r1, r0)){
          printf("Tie.\n");
        } else if (min(s1, s0) > min(r1, r0)){
          printf("Player 1 wins.\n");
        } else {
          printf("Player 2 wins.\n");
        }
      } else {
        if (max(s1, s0) > max(r1, r0)){
          printf("Player 1 wins.\n");
        } else {
          printf("Player 2 wins,\n");
        }
      } 
    }
  }

  return 0;
}
