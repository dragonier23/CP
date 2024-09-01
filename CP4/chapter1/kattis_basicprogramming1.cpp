#include <bits/stdc++.h>

using namespace std;

int main() {
  int N, t;
  scanf("%d %d", &N, &t);

  int A[N];
  for (int i = 0; i < N; i++){
    scanf("%d ", &A[i]);
  }

  if (t == 1){
    printf("7");
  }

  else if (t == 2){
    if (A[0] > A[1]){
      printf("Bigger");
    } else if (A[0] == A[1]){
      printf("Equal");
    } else {
      printf("Smaller");
    }
  }

  else if (t == 3){
    if (A[0] == A[1] || A[1] == A[2]){
      printf("%d", A[1]);
    }
    else if (A[0] == A[2]){
      print("%d", A[0]);
    }
    else {
      int maximum, minimum;
      maximum = max(A[0], max(A[1], A[2]));
      minimum = min(A[0], min(A[1], A[2]));

      if (A[0] != maximum && A[0] != minimum){
        printf("%d", A[0]);
      } else if (A[1] != maximum && A[1] != minimum){
        printf("%d", A[1]);
      } else {
        printf("%d", A[2]);
      }
    }
  }

  else if (t == 4){
    int sum = 0;
    for (int i = 0; i < N; i++){
      sum += A[i];
    }
    printf("%d", sum);
  }

  else if (t == 5){
    int sum = 0;
    for (int i = 0; i < N; i++){
      if (A[i] % 2 == 0){
        sum += A[i];
      }
    }
    printf("%d", sum);
  }

  else if (t == 6){
    for (int i = 0; i < N; i++){
      cout << char((A[i] % 26) + 97);
    }

  }

  else{
    bool within[N];
    for (int i = 0; i < N; i++){
      within[i] == false;
    }
    int curr = 0;
    while (true){
      if (curr >= N){
        printf("Out");
        break;
      } else if (curr == (N-1)){
        printf("Done");
        break;
      } else if (within[curr]){
        printf("Cyclic");
        break;
      } else {
        within[curr] = true;
        curr = A[curr];
      }
    }
  }

  return 0;
}
