#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct type_chanson {
  int annee;
  char *titre;
  char *chanteur;
} chanson;

void liberer(chanson *cat) {
  free(cat->titre);
  free(cat->chanteur);
  free(cat);
}

chanson *supprimer(chanson *cat, int *taille, char *t) {
  int i = 0;
  while (i < *taille) {
    if (strcmp(cat[i].titre, t) == 0) {
      for (int j = i; j < *taille; j++) {
        cat[j] = cat[j + 1];
      }
      *taille = *taille - 1;
      return cat;
    }
    i++;
  }
  return cat;
}

chanson *ajouter(chanson *cat, int *taille, chanson s) {
    cat = realloc(cat, sizeof(chanson));
    cat[*taille].chanteur = (char *)malloc(30 * sizeof(char));
    cat[*taille].titre = (char *)malloc(30 * sizeof(char));
    cat[*taille].chanteur = s.chanteur;
    cat[*taille].titre = s.titre;
    cat[*taille].annee = s.annee;
    *taille = *taille + 1;

    printf("%d", *taille);
    printf("%s", cat[1].chanteur);

    return cat;
}

void afficher(chanson *cat, int taille) {
    for (int i = 0; i<taille; i++) {
        printf("Le chanteur de la chanson %d est: %s \n", i, cat[i].chanteur);
        printf("Le titre de la chanson %d est: %s \n", i, cat[i].titre);
        printf("L'annee de sortie de la chanson %d est: %d \n", i, cat[i].annee);
    }
}

int main() {
    int *taille = (int *)malloc(sizeof(int));
    chanson s;
    printf("Entrez la taille du catalogue: ");
    scanf("%d", taille);
    chanson *cat = (chanson *)malloc(sizeof(chanson) * *taille);
    for (int i=0; i<*taille; i++) {
        cat[i].chanteur = (char *)malloc(30 * sizeof(char));
        cat[i].titre = (char *)malloc(30 * sizeof(char));
        printf("Entrez le nom du chanteur: ");
        scanf("%s", cat[i].chanteur);
        printf("Entrez le titre de la chanson: ");
        scanf("%s", cat[i].titre);
        printf("Entrez l'annee de sortie de la chanson: ");
        scanf("%d", &cat[i].annee);
    }
    s.chanteur = (char *)malloc(30 * sizeof(char));
    s.titre = (char *)malloc(30 * sizeof(char));
    printf("Entrez le nom du chanteur a ajouter: ");
    scanf("%s", s.chanteur);
    printf("Entrez le titre de la chanson a ajouter: ");
    scanf("%s", s.titre);
    printf("Entrez l'annee de sortie de la chanson a ajouter: ");
    scanf("%d", &s.annee);
    ajouter(cat, taille, s);
    afficher(cat, *taille);
    

    return 0;
}