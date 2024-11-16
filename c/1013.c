#include <stdio.h>
#include <stdlib.h>

int maior_ab(int a, int b);

int main(){

    int x, y, z;

    scanf("%d %d %d", &x, &y, &z);

    printf("%d eh o maior\n", maior_ab(maior_ab(x, y), z));
}

int maior_ab(int a, int b){

    return (a + b + abs(a - b))/2;
}