#include <stdio.h>

int main(){
    int c, p,f;

    scanf("%d %d %d", &c, &p, &f);

    char result = ((c * f) <= p) ? 'S' : 'N';

    printf("%c\n", result);

    return 0;
}