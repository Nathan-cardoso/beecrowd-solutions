#include <stdio.h>

void mostrarResultado(int a, int b);

int main(){
    int p1, c1, p2, c2;

    scanf("%d %d %d %d", &p1, &c1, &p2, &c2);

    int result1 = p1 * c1;
    int result2 = p2 * c2;

    mostrarResultado(result1, result2);

    return 0;
}

void mostrarResultado(int a, int b){
    if(a == b){
        printf("0\n");
    } else if(a > b){
        printf("-1\n");
    }else{
        printf("1\n");
    }
}