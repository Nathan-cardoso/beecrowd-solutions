#include <stdio.h>

int main(){
    int cod, qtd;
    float preco, contaFinal;

    scanf("%d%d", &cod, &qtd);

    switch (cod)
    {
    case 1 :
        preco = 4.;
        contaFinal = preco * qtd;
        break;
    case 2 :
        preco = 4.50;
        contaFinal = preco * qtd;
        break;
    case 3 :
        preco = 5.;
        contaFinal = preco * qtd;
        break;
    case 4 :
        preco = 2.;
        contaFinal = preco * qtd;
        break;
    case 5 :
        preco = 1.50;
        contaFinal = preco * qtd;
        break;   
    default:
        break;
    }

    printf("Total: R$ %.2f\n",contaFinal);


    return 0;
}