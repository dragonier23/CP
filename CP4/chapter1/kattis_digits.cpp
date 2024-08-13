#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <cmath>
#include <vector>

using namespace std;

int main() {
  string input, curr;
  int count; 

  while (true){
    cin >> input;
    if (input == "END"){
      break;
    }
    count = 0;
    while (true){
      curr = to_string(input.length());
      if (curr == input){
        count++;
        break;
      }
      input = curr;
      count++;
    }
    printf("%d\n", count);
  }

  return 0;
}
