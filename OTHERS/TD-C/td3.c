#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define DIMENSION 2

struct carte {
  float re;
  float im;
};

struct pola {
  float mod;
  float arg;
};

struct cplx {
  struct carte car;
  struct pola pol;
};

void ex35() {
  int indA, indB, temp;
  int tab[5] = {25, 22, 36, 64, 2};
  printf("Entrez la position du premier élement: ");
  scanf("%d", &indA);
  printf("Entrez la position du second élement: ");
  scanf("%d", &indB);
  printf("Avant: \n");
  for (int i = 0; i < 4; i++) {
    printf("%d ", tab[i]);
  }
  printf("\nAprès: \n");
  temp = tab[indA - 1];
  tab[indA - 1] = tab[indB - 1];
  tab[indB - 1] = temp;
  for (int i = 0; i < 4; i++) {
    printf("%d ", tab[i]);
  }
}

void ex36() {
  char phrase[100] = "J'adore vraiment La matière NF06 Elle Est ma pref";
  int sum = 0;
  for (int i = 0; i < 100; i++) {
    if ((phrase[i] > 64) && (phrase[i] < 91)) {
      sum += 1;
    }
  }
  printf("%d", sum);
}

void ex37() {
  float summ;
  float mat1[DIMENSION][DIMENSION] = {{1, 2}, {3, 2}};
  float mat2[DIMENSION][DIMENSION] = {{4, 6}, {3, 1}};
  float sum[DIMENSION][DIMENSION], sub[DIMENSION][DIMENSION],
      mul[DIMENSION][DIMENSION];
  printf("Somme: \n");
  for (int i = 0; i < DIMENSION; i++) {
    for (int j = 0; j < DIMENSION; j++) {
      sum[i][j] = mat1[i][j] + mat2[i][j];
      printf("%f ", sum[i][j]);
    }
    printf("\n");
  }
  printf("Soustraction: \n");
  for (int i = 0; i < DIMENSION; i++) {
    for (int j = 0; j < DIMENSION; j++) {
      sub[i][j] = mat1[i][j] + mat2[i][j];
      printf("%f ", sub[i][j]);
    }
    printf("\n");
  }
  printf("Multiplication: \n");
  for (int j = 0; j < DIMENSION; j++) {
    for (int i = 0; i < DIMENSION; i++) {
      summ = 0;
      for (int a = 0; a < DIMENSION; a++) {
        summ += mat1[j][a] * mat2[a][i];
      }
      mul[j][i] = summ;
      printf("%f ", mul[j][i]);
    }
    printf("\n");
  }
}

struct pola carte2pola(struct carte nb) {
  struct pola pol;
  pol.mod = sqrt(nb.im * nb.im + nb.re * nb.re);
  pol.arg = atan(nb.im / nb.re);
  return pol;
}

struct carte pola2carte(struct pola nb) {
  struct carte cart;
  cart.re = nb.mod * cos(nb.arg);
  cart.im = nb.mod * sin(nb.arg);
  return cart;
}

struct carte SommeCplx(struct carte nb1, struct carte nb2) {
  struct carte somme;
  somme.re = nb1.re + nb2.re;
  somme.im = nb1.im + nb2.im;
  return somme;
}

struct carte SousCplx(struct carte nb1, struct carte nb2) {
  struct carte sous;
  sous.re = nb1.re - nb2.re;
  sous.im = nb1.im - nb2.im;
  return sous;
}

struct carte MulCplx(struct carte nb1, struct carte nb2) {
  struct carte produit;
  produit.re = nb1.re * nb2.re + nb1.im * nb2.im * (-1);
  produit.im = nb1.re * nb2.im + nb1.im * nb2.re;
  return produit;
}

struct carte DivCplx(struct carte nb1, struct carte nb2) {
  struct pola divPola;
  divPola.mod = carte2pola(nb1).mod / carte2pola(nb2).mod;
  divPola.arg = carte2pola(nb1).arg - carte2pola(nb2).arg;
  return pola2carte(divPola);
}

void ResoudreEq(struct carte coefs[3]) {
  struct carte delta, sqrtDelta;
  struct pola sqrtDeltaPola;
  struct carte x1, x2;
  struct carte minusOne = {-1, 0};
  struct carte two = {2, 0};
  struct carte four = {4, 0};
  delta = SousCplx(MulCplx(coefs[1], coefs[1]),
                   MulCplx(MulCplx(four, coefs[0]), coefs[2]));
  printf("%f \n", delta.re);
  printf("%f \n", delta.im);
  sqrtDeltaPola.mod = sqrt(carte2pola(delta).mod);
  sqrtDeltaPola.arg = 0.5 * carte2pola(delta).arg;
  sqrtDelta = pola2carte(sqrtDeltaPola);
  printf("%f \n", sqrtDelta.re);
  printf("%f \n", sqrtDelta.im);
  x1 = DivCplx(SommeCplx(MulCplx(minusOne, coefs[1]), sqrtDelta),
               MulCplx(two, coefs[0]));
  x2 = DivCplx(SousCplx(MulCplx(minusOne, coefs[1]), sqrtDelta),
               MulCplx(two, coefs[0]));
  printf("%f \n", x1.re);
  printf("%f \n", x1.im);
  printf("%f \n", x2.re);
  printf("%f \n", x2.im);
}

void ex38() {
  struct carte nbA, nbB, coefs[3];
  printf("Entrez partie réelle: ");
  scanf("%f", &nbA.re);
  printf("Entrez partie imaginaire: ");
  scanf("%f", &nbA.im);
  printf("Entrez partie réelle: ");
  scanf("%f", &nbB.re);
  printf("Entrez partie imaginaire: ");
  scanf("%f", &nbB.im);
  printf("%f \n", carte2pola(nbA).mod);
  printf("%f \n", carte2pola(nbA).arg);
  printf("\n");
  printf("%f \n", pola2carte(carte2pola(nbA)).re);
  printf("%f \n", pola2carte(carte2pola(nbA)).im);
  printf("\n");
  printf("%f \n", SommeCplx(nbA, nbB).re);
  printf("%f \n", SommeCplx(nbA, nbB).im);
  printf("\n");
  printf("%f \n", SousCplx(nbA, nbB).re);
  printf("%f \n", SousCplx(nbA, nbB).im);
  printf("\n");
  printf("%f \n", MulCplx(nbA, nbB).re);
  printf("%f \n", MulCplx(nbA, nbB).im);
  printf("\n");
  printf("%f \n", DivCplx(nbA, nbB).re);
  printf("%f \n", DivCplx(nbA, nbB).im);
  printf("Entrez la partie réelle du coef de x^2: ");
  scanf("%f", &coefs[0].re);
  printf("Entrez la partie imaginaire du coef de x^2: ");
  scanf("%f", &coefs[0].im);
  printf("Entrez la partie réelle du coef de x: ");
  scanf("%f", &coefs[1].re);
  printf("Entrez la partie imaginaire du coef de x: ");
  scanf("%f", &coefs[1].im);
  printf("Entrez la partie réelle de la constante: ");
  scanf("%f", &coefs[2].re);
  printf("Entrez la partie imaginaire de la constante: ");
  scanf("%f", &coefs[2].im);
  ResoudreEq(coefs);
}

int main(void) {
  int exo;
  printf("Quel exercice ? ");
  scanf("%d", &exo);
  switch (exo) {
  case 35:
    ex35();
    break;
  case 36:
    ex36();
    break;
  case 37:
    ex37();
    break;
  case 38:
    ex38();
    break;
  }
  return 0;
}