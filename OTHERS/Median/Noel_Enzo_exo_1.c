#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void coder(int d, char* source, char* destination) {
    FILE *fileptrsrc;
    FILE *fileptrdest;
    char temp;
    fileptrsrc = fopen(source, "r+");
    fileptrdest = fopen(destination, "w+");
    while (feof(fileptrsrc)==0) {
        fscanf(fileptrsrc, "%c", &temp);
        fprintf(fileptrdest, "%c", (temp+d)%128);
    };
    fclose(fileptrsrc);
    fclose(fileptrdest);
}

int main() {
    char *source, *dest;
    int d;
    source = malloc(sizeof(char)*30);
    dest = malloc(sizeof(char)*30);
    printf("Entrez le nom du fichier source: ");
    scanf("%s", source);
    printf("Entrez le nom du fichier de destination: ");
    scanf("%s", dest);
    printf("Entrez le décalage des lettres: ");
    scanf("%d", &d);
    coder(d, source, dest);
    return 0;
}