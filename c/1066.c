//Pares, Ímpares, Positivos e Negativos

#include <stdio.h>

int main(){
    int n[5];
    int par = 0, impar = 0;
    int positivo = 0, negativo = 0;

    for (int i = 0; i < 5; i++)
    {
        scanf("%i", i + n);

        if(n[i] % 2 == 0){
            par++;
        }else{
            impar++;
        }

        if(n[i] > 0){
            positivo++;
        }else{
            negativo++;
        }
    }
    printf("%i valor(es) par(es)\n",par);
    printf("%i valor(es) impar(es)\n",impar);
    printf("%i valor(es) positivo(s)\n",positivo);
    printf("%i valor(es) negativo(s)\n",negativo);
  


    return 0;
}