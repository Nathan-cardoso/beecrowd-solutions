#include <stdio.h>

int main(){
    int input;
    int r1, r2;

    scanf("%d", &input);
    int result[input];

    for(int i = 0; i < input; i++){
        scanf("%d %d", &r1, &r2);
        result[i] = r1 + r2;
    }

    for(int i = 0; i < input; i++){
        printf("%d\n", result[i]);
    }

    return 0;
}