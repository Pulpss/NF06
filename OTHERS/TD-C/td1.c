#include <stdio.h>
#include <time.h>

void ex1() {
  time_t t = time(NULL);
  struct tm tm = *localtime(&t);
  printf("Hello World\n");
  printf("La date est: %02d/%02d/%d \n", tm.tm_mday, tm.tm_mon + 1, tm.tm_year + 1900);
  int week = ((tm.tm_yday + 1)-(tm.tm_yday + 1)%7)/7+1;
  printf("Nous sommes la semaine: %d \n", week);
  printf("prenom.nom@ecole.fr");
}

void ex2() {
  int i = 2; // il a fallu modifier cette ligne pour que le programme marche
  int j = 5;

  // Division de j par i
  printf("Division de j par i = %d", j / i);
}

void ex3() {
  printf("La taille du type int est: %d \n", sizeof(int));
  printf("La taille du type short est: %d \n", sizeof(short));
  printf("La taille du type char est: %d \n", sizeof(char));
  printf("La taille du type float est: %d \n", sizeof(float));
  printf("La taille du type double est: %d \n", sizeof(double));
}

void ex4() {
  unsigned short A = 104;
  unsigned short B;
  float C = 6.5;

  A += (unsigned short) C;
  A = ~A;
  B = A^(A+2);
  C = (float) (A<<B);
  A = A&(unsigned short) C;

  printf("%d", A);
}

void ex5() {
  int x, p, n;
  printf("X: ");
  scanf("%d", &x);
  printf("P: ");
  scanf("%d", &p);
  printf("N: ");
  scanf("%d", &n);
  int mask = ~((~0<<p)<<n-1);
  printf("%d", x^mask-1);
}


//
int main(void) {
  int exo;
  printf("Quel exercice ? \n");
  scanf("%d", &exo);
  if (exo == 1) {
    ex1();
  } else if (exo == 2) {
    ex2();
  } else if (exo == 3) {
    ex3();
  } else if (exo == 4) {
    ex4();
  } else if (exo == 5) {
    ex5();
  }
  return 0;
}