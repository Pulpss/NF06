#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ex50() {
  char name[20];
  FILE *fileptr;
  int M;
  int N;
  float **vecteurs;
  float coefTemp;
  char charTemp;
  printf("Input a filename: ");
  scanf("%s", name);
  printf("Entrez la taille de vos vecteurs: ");
  scanf("%d", &N);
  printf("Entrez le nombre de vecteurs: ");
  scanf("%d", &M);
  fileptr = fopen(name, "w");
  for (int i = 0; i < M; ++i) {
    for (int j = 0; j < N; ++j) {
      printf("Pour le vecteur %d, entrez le coefficient %d: ", i + 1, j + 1);
      scanf("%f", &coefTemp);
      fprintf(fileptr, "%.2f ", coefTemp);
    }
    fprintf(fileptr, "\n");
  }
  fclose(fileptr);
  printf("Maintenant je vais faire la somme des vecteurs. \n");
  vecteurs = (float **)calloc(N, sizeof(float *));
  if (vecteurs != NULL) {
    for (int i = 0; i < N; ++i) {
      vecteurs[i] = (float *)calloc(M, sizeof(float));
    }
  }
  fileptr = fopen(name, "r");
  char nombreTemp[4];
  for (int i = 0; i < M; ++i) {
    for (int j = 0; j < N; ++j) {
      fscanf(fileptr, "%c", &nombreTemp[0]);
      fscanf(fileptr, "%c", &nombreTemp[1]);
      fscanf(fileptr, "%c", &nombreTemp[2]);
      fscanf(fileptr, "%c", &nombreTemp[3]);
      vecteurs[i][j] = atof(nombreTemp);
      fscanf(fileptr, "%c", &charTemp); // lespace
    }
  }
  fclose(fileptr);
  fileptr = fopen(name, "r+");
  float somme;
  for (int i = 0; i < N; ++i) {
    somme = 0;
    for (int j = 0; j < M; ++j) {
      somme += vecteurs[j][i];
    }
    printf("%.2f ", somme);
    fseek(fileptr, 21, SEEK_END);
    fprintf(fileptr, "%.2f ", somme);
  }
  fclose(fileptr);
}

int main(void) {
  int exo;
  printf("Quel exercice ? ");
  scanf("%d", &exo);
  switch (exo) {
  case 50:
    ex50();
    break;
  }
  return 0;
}