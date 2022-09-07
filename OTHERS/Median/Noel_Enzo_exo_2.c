#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void inserer(int tab[], int *taille, int nb){
    int i = 0;
    while (i < *taille && tab[i] < nb){
        i++;
    }
    for (int j = *taille; j > i; j--){
        tab[j] = tab[j-1];
    }
    tab[i] = nb;
    *taille = *taille + 1;
}

int main() {
    int tab[100], nb;
    int *taille = (int *)malloc(sizeof(int));

    printf("Entrez la taille du tableau initital: ");
    scanf("%d", taille);
    for (int i = 0; i<*taille; i++) {
        printf("Entrez l'element, %d du tableau: ", i);
        scanf("%d", &tab[i]);
    }

    printf("Quel chiffre voulez vous inserer: ");
    scanf("%d", &nb);

    inserer(tab, taille, nb);

    for (int i = 0; i<*taille; i++) {
        printf("%d ", tab[i]);
    }

    return 0;
}