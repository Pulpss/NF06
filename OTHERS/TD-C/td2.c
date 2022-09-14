#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define max(a, b) (a > b) ? a : b

int prime(int n) {
  if (n == 2)
    return 1;
  else {
    int k = 2;
    int z = 1;
    while (k < n) {
      while ((prime(k) == 0) && (k < n - 1)) {
        k++;
      };
      if (n % k == 0) {
        z = 0;
        k++;
      } else
        k++;
    };
    return z;
  };
}

void ex16() {
  int i;
  for (i = 2; i < 50; i++) {
    printf("prime (%d) = %d  \n", i, prime(i));
  }
}

int findMax(int tab[100], int taille) {
  int maxi = tab[0];
  for (int i = 0; i < taille; i++) {
    maxi = max(maxi, tab[i]);
  }
  return maxi;
}

void ex17() {
  int input, taille, tab[100];
  printf("Entrez la taille du tableau \n");
  scanf("%d", &taille);
  printf("Entrez les nombres à la suite \n");
  for (int i = 0; i < taille; i++) {
    scanf("%d", &tab[i]);
  }
  printf("Le max est %d", findMax(tab, taille));
}

int zero(int nombre) {
  if (nombre < 10) {
    return 0;
  } else if (nombre % 10 == 0) {
    return 1;
  } else {
    return zero((nombre - nombre % 10) / 10);
  }
}

void ex18() {
  int nombre;
  printf("Entrez votre nombre \n");
  scanf("%d", &nombre);
  printf("Votre nombre %s zéro", zero(nombre) ? "contient un" : "ne contient pas de");
}

void ex19() {
  float a, b, c, delta;
  printf("Pour une fonction de la forme ax^2 + bx + c : \n");
  printf("Entrez a: ");
  scanf("%f", &a);
  printf("Entrez b: ");
  scanf("%f", &b);
  printf("Entrez c: ");
  scanf("%f", &c);
  delta = b*b - 4*a*c;
  delta < 0 ? printf("Votre polynome n'a pas de racines") : delta == 0 ? printf("La seule racine de votre polynome est %f", (-1*b)/(2*a)) : printf("Les racines de votre polynome sont %f et %f", (-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a));
  
}

int fiboIter(int nbt) {
  int temp;
  int terma = 0;
  int termb = 1;
  for (int i=0; i<nbt-1; i++) {
    temp = termb;
    termb = termb + terma;
    terma = temp;
  }
  return terma;
}

int fiboRecur(int nbt) {
  if (nbt == 0) {
    return 0;
  } else if (nbt == 1) {
    return 1;
  } else {
    return fiboRecur(nbt-1)+fiboRecur(nbt-2);
  }
}

void ex20() {
  int nbt;
  printf("Entrez le terme que vous voulez \n");
  scanf("%d", &nbt);
  printf("Le terme %d de la suite de Fibonacci par itérativité est %d \n", nbt, fiboIter(nbt));
  printf("Le terme %d de la suite de Fibonacci par recursivité est %d \n", nbt, fiboIter(nbt+1));
}

int main(void) {
  int exo;
  printf("Quel exercice ? ");
  scanf("%d", &exo);
  switch (exo) {
  case 16:
    ex16();
    break;
  case 17:
    ex17();
    break;
  case 18:
    ex18();
    break;
  case 19:
    ex19();
    break;
  case 20:
    ex20();
    break;
  }
  return 0;
}