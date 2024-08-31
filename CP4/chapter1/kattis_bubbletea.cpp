#include <bits/stdc++.h>

using namespace std;

int main() {
  int m, n;

  scanf("%d", &n);
  int nlist[n];
  for (int i = 0; i < n; i++){
    scanf("%d ", &nlist[i]);
  }

  scanf("%d", &m);
  int mlist[m];
  for (int i = 0; i < m; i++){
    scanf("%d ", &mlist[i]);
  }

  int min = 1e9;
  for (int i = 0; i < n; i++){
    int k;
    scanf("%d ", &k);
    for (int j = 0; j < k; j++){
      int x;
      scanf("%d ", &x);
      int curr = nlist[i] + mlist[x - 1];
      if (curr < min){
        min = curr; 
      }
    }
  }

  int money;
  scanf("%d", &money);

  int ans = (money / min);
  printf("%d", ans > 0 ? ans - 1 : 0);

  return 0;
}
