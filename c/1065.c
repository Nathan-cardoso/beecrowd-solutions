//Resolução do problema 1065
//Pares entre Cinco Números

#include <stdio.h>

int main(){
    int vet[5];
    int par = 0;

    for(int i=0; i < 5;i++){
        scanf("%i", i + vet);
        if(vet[i] % 2 == 0){
            par++;
        }
    }

    printf("%i valores pares\n",par);

    return 0;
}