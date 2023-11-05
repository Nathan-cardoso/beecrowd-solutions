#include <stdio.h>

int main(){
    
    int vet[5];
     vet[0]  = 300;
     vet[1]  = 1500;
     vet[2]  = 600;
     vet[3]  = 1000;
     vet[4]  = 150;

    for(int i = 0; i < 5; i++){
        int input;
        scanf("%d", &input);
        vet[i] *= input;
    }

    int soma = 0;

    for(int i = 0; i < 5; i++){
        soma += vet[i];
    }

    soma += 225;

    printf("%i\n", soma);


    return 0;
}