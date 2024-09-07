#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;

  cin >> s; 

  int len = s.length(), sum = 0 + 'R' + 'B' + 'L';
    
  int tmp = 0; 
  while (tmp < len - 2){
    if (s[tmp] + s[tmp + 1] + s[tmp + 2] == sum){
      cout << 'C';
      tmp += 3;
    } else {
      char ans = (s[tmp] == 'R') ? char('S') : ((s[tmp] == 'B') ? char('K') : char('H'));
      cout << ans;
      tmp++;
    }
  }
  if (tmp < len){
    while (tmp < len){
      char ans = (s[tmp] == 'R') ? char('S') : ((s[tmp] == 'B') ? char('K') : char('H'));
      cout << ans;
      tmp++;
    }
  }
  cout << endl;

  return 0;
}
