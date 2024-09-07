#include <bits/stdc++.h>

using namespace std;

int main() {
  int N, t;
  scanf("%d %d", &N, &t);

  long long A[N];
  for (int i = 0; i < N; i++){
    scanf("%lld ", &A[i]);
  }

  if (t == 1){
    printf("7\n");
  }

  else if (t == 2){
    if (A[0] > A[1]){
      printf("Bigger\n");
    } else if (A[0] == A[1]){
      printf("Equal\n");
    } else {
      printf("Smaller\n");
    }
  }

  else if (t == 3){
    printf("%lld\n", A[0] + A[1] + A[2] - max(max(A[0], A[1]), A[2]) - min(min(A[0], A[1]), A[2]));
  }

  else if (t == 4){
    long long sum = 0;
    for (int i = 0; i < N; i++){
      sum += A[i];
    }
    printf("%lld\n", sum);
  }

  else if (t == 5){
    long long sum = 0;
    for (int i = 0; i < N; i++){
      if (A[i] % 2 == 0){
        sum += A[i];
      }
    }
    printf("%lld\n", sum);
  }

  else if (t == 6){
    for (int i = 0; i < N; i++){
      cout << char('a' + A[i] % 26);
    }
    cout << endl;
  }

  else{
    bool within[N];
    for (int i = 0; i < N; i++){
      within[i] == false;
    }
    long long curr = 0;
    while (true){
      if (curr >= N){
        printf("Out\n");
        break;
      } else if (within[curr]){
        printf("Cyclic\n");
        break;
      } else if (curr == (N-1)){
        printf("Done\n");
        break;
      } else {
        within[curr] = true;
        curr = A[curr];
      }
    }
  }

  return 0;
}

