#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  int tmp, s0, s1, r0, r1;
  while (scanf("%d %d %d %d", &s0, &s1, &r0, &r1), (s1 || s0 || r0 || r1)){
    if (s0 < s1){
      tmp = s0;
      s0 = s1; 
      s1 = tmp;
    }

    if (r0 < r1){
      tmp = r0;
      r0 = r1;
      r1 = tmp; 
    }

    if ((s1 == 1 && s0 == 2) && (r1 == 1 && r0 == 2)){
      printf("Tie.\n");
    } 
    else if (s1 == 1 && s0 == 2){
      printf("Player 1 wins.\n");
    } 
    else if (r1 == 1 && r0 == 2){
      printf("Player 2 wins.\n");
    } 

    else if (s1 == s0 && r1 == r0){
      if (s0 == r0){
        printf("Tie.\n");
      } 
      else {
        printf("Player %d wins.\n", (r0 > s0) ? 2 : 1);
      }
    } 

    else if (s1 == s0) {
      printf("Player 1 wins.\n");
    } 

    else if (r1 == r0) {
      printf("Player 2 wins.\n");
    } 

    else {
      if (s0 > r0){
        printf("Player 1 wins.\n");
      }
      else if (s0 < r0){
        printf("Player 2 wins.\n");
      }
      else {
        if (s1 > r1){
          printf("Player 1 wins.\n");
        }
        else if (s1 < r1){
          printf("Player 2 wins.\n");
        }
        else{
          printf("Tie.\n");
        }
      }
    }
  }

  return 0;
}
