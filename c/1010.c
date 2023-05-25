//Resolução do problema 1010

#include <stdio.h>

int main(){
    int cod1, cod2, qtd1, qtd2;
    float preco1, preco2;
    scanf("%i %i %f", &cod1, &qtd1, &preco1);
    scanf("%i %i %f", &cod2, &qtd2, &preco2);

    float precoTotal = (qtd1 * preco1) + (qtd2 * preco2);

    printf("VALOR A PAGAR: R$ %.2f\n", precoTotal);

    return 0;
}