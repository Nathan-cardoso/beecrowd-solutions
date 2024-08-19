#include <stdio.h>

int main(){

    float numX, numY;

    scanf("%f %f", &numX, &numY);

    if(numX > 0.0 && numY > 0.0){
        printf("Q1\n");
    }
    else if(numX < 0.0 && numY > 0.0){
        printf("Q2\n");
    }
    else if(numX < 0.0 && numY < 0.0){
        printf("Q3\n");
    }
    else if(numX > 0.0 && numY < 0.0){
        printf("Q4\n");
    }
    else if((numX < 0.0 || numX > 0.0) && numY == 0.0){
        printf("Eixo X\n");
    }
    else if((numY < 0.0 || numY > 0.0) && numX == 0.0){
        printf("Eixo Y\n");
    }
    else{
        printf("Origem\n");
    }

    return 0;
}