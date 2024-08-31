#include <bits/stdc++.h>

using namespace std;

int main() {
  int n; 
  scanf("%d", &n);

  // we start with 3, increase by 1 each time 
  printf("%d", (n > 3) ? n - 2 : 1);
  return 0;
}
