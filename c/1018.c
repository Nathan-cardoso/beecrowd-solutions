#include <stdio.h>

int main()
{
    int value;

    scanf("%d", &value);

    printf("%d\n",value);

    int vet[7] = {100, 50, 20, 10, 5, 2, 1};
    int rating[7];

    for (int i = 0; i < 7; i++)
    {
        rating[i] = (int)value / vet[i];
        value = value - (rating[i] * vet[i]);
    }

    for(int j = 0; j < 7; j++){
        printf("%d nota(s) de R$ %d,00\n",rating[j], vet[j]);
    }
}