#include <stdio.h>

int main()
{
    int number, horas;
    float hrTrabalho;

    scanf("%d %d %f", &number, &horas, &hrTrabalho);

    printf("NUMBER = %d\nSALARY = U$ %.2f\n", number, (horas * hrTrabalho));
}