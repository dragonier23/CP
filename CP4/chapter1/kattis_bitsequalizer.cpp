#include <bits/stdc++.h>

using namespace std;

int main() {
  int c;
  string s, t;
  scanf("%d", &c);

  for (int i = 0; i < c; i++){
    cin >> s;
    cin >> t;
    int sZeroCount = 0, tZeroCount = 0, sQCount = 0, sOneCount = 0, tOneCount = 0, len = s.length();
    for (int j = 0; j < len; j++){
      if (s[j] == '0'){
        sZeroCount++;
      } else if (s[j] == '?'){
        sQCount++;
      } else {
        sOneCount++;
      }

      if (t[j] == '0'){
        tZeroCount++;
      } else {
        tOneCount++;
      }
    }
    if (sZeroCount + sQCount < tZeroCount){
      cout << "Case " << i + 1 << ": " << -1; 
    }
  }


  return 0;
}
