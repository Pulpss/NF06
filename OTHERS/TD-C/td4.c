#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct etudiant {
  float median;
  float final;
  float moyenne;
  char *nom;
  char *prenom;
} etudiant;

float *sommeVec(float *vec1, float *vec2) {
  float taille1 = sizeof(*vec1) / sizeof(float);
  float taille2 = sizeof(*vec2) / sizeof(float);
  float *somme;
  if (taille1 != taille2) {
    return 0;
  }
  somme = malloc(sizeof(float) * taille1);
  for (int i = 0; i < taille1 + 1; ++i) {
    somme[i] = vec1[i] + vec2[i];
  }
  return somme;
}

float *sousVec(float *vec1, float *vec2) {
  float taille1 = sizeof(*vec1) / sizeof(float) + 1;
  float taille2 = sizeof(*vec2) / sizeof(float) + 1;
  float *somme;
  if (taille1 != taille2) {
    return 0;
  }
  somme = malloc(sizeof(float) * taille1);
  for (int i = 0; i < taille1; ++i) {
    somme[i] = vec1[i] - vec2[i];
  }
  return somme;
}

float produitScal(float *vec1, float *vec2) {
  float taille1 = sizeof(*vec1) / sizeof(float) + 1;
  float taille2 = sizeof(*vec2) / sizeof(float) + 1;
  float somme = 0;
  if (taille1 != taille2) {
    return 0;
  }
  for (int i = 0; i < taille1; ++i) {
    somme += vec1[i] * vec2[i];
  }
  return somme;
}

void ex46() {
  int taille;
  float *vec1, *vec2, *somme, *sous, coef;
  printf("Quelle est la taille de votre vecteur : ");
  scanf("%d", &taille);
  vec1 = malloc(sizeof(float) * taille);
  for (int i = 0; i < taille; ++i) {
    printf("Quelle est le coef %d : ", i + 1);
    scanf("%f", &vec1[i]);
  }
  vec2 = malloc(sizeof(float) * taille);
  for (int i = 0; i < taille; ++i) {
    printf("Quelle est le coef %d : ", i + 1);
    scanf("%f", &vec2[i]);
  }
  somme = sommeVec(vec1, vec2);
  for (int i = 0; i < taille; ++i) {
    printf("%f \n", somme[i]);
  }
  sous = sousVec(vec1, vec2);
  for (int i = 0; i < taille; ++i) {
    printf("%f \n", sous[i]);
  }
  printf("Le produit scalaire est %f", produitScal(vec1, vec2));
}

void swapEtudiants(etudiant *etudiants, int i) {
  float tempNum;
  char *tempA = (char *)malloc(30 * sizeof(char));
  char *tempB = (char *)malloc(30 * sizeof(char));
  tempA = etudiants[i].prenom;
  tempB = etudiants[i + 1].prenom;
  etudiants[i + 1].prenom = tempA;
  etudiants[i].prenom = tempB;

  tempA = etudiants[i].nom;
  tempB = etudiants[i + 1].nom;
  etudiants[i + 1].nom = tempA;
  etudiants[i].nom = tempB;

  etudiants[i].median = tempNum;
  etudiants[i].median = etudiants[i + 1].median;
  etudiants[i + 1].median = tempNum;

  etudiants[i].final = tempNum;
  etudiants[i].final = etudiants[i + 1].final;
  etudiants[i + 1].final = tempNum;

  etudiants[i].moyenne = tempNum;
  etudiants[i].moyenne = etudiants[i + 1].moyenne;
  etudiants[i + 1].moyenne = tempNum;
}

void sort(etudiant *etudiants, int taille) {
  for (int i = 0; i < taille; i++) {
    for (int j = 0; j < taille - 1; j++) {
      if (strcmp(etudiants[j].nom, etudiants[j + 1].nom) > 0) {
        swapEtudiants(etudiants, j);
      } else if (strcmp(etudiants[j].nom, etudiants[j + 1].nom) == 0 &&
                 strcmp(etudiants[j].prenom, etudiants[j + 1].prenom) > 0) {
        swapEtudiants(etudiants, j);
      }
    }
  }
}

void triEtudiants(etudiant *etudiants, int taille) {
  sort(etudiants, taille);
  printf("Les etudiants triés par ordre alphabétique sont \n");
  for (int i = 0; i < taille; ++i) {
    printf("Etudiant : %d \n", i + 1);
    printf("Prénom : %s \n", etudiants[i].prenom);
    printf("Nom: %s \n", etudiants[i].nom);
    printf("Note au médian : %f \n", etudiants[i].median);
    printf("Note au final : %f \n", etudiants[i].final);
    printf("Moyenne :%f \n", etudiants[i].moyenne);
  }
}

void ex47() {
  int taille;
  etudiant *etudiants;
  printf("Quelle est la taille de votre liste d'étudiants : ");
  scanf("%d", &taille);
  etudiants = malloc(sizeof(etudiant) * taille);
  for (int i = 0; i < taille; ++i) {
    etudiants[i].prenom = malloc(sizeof(char) * 30);
    etudiants[i].nom = malloc(sizeof(char) * 30);
    printf("Entrez le prenom de l'étudiant : ");
    scanf("%s", etudiants[i].prenom);
    printf("Entrez le nom de l'étudiant : ");
    scanf("%s", etudiants[i].nom);
    printf("Entrez la note du médian de l'étudiant : ");
    scanf("%f", &etudiants[i].median);
    printf("Entrez la note du final de l'étudiant : ");
    scanf("%f", &etudiants[i].final);
    etudiants[i].moyenne = 0.6 * etudiants[i].final + 0.4 * etudiants[i].median;
  }
  triEtudiants(etudiants, taille);
}

int main(void) {
  int exo;
  printf("Quel exercice ? ");
  scanf("%d", &exo);
  switch (exo) {
  case 46:
    ex46();
    break;
  case 47:
    ex47();
    break;
  }
  return 0;
}