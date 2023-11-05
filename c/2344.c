#include <stdio.h>

int main(){
    int notaNum;
    char notaLetra;

    scanf("%d",&notaNum);

    if(notaNum == 0){
        notaLetra = 'E';
    }else if(notaNum >= 1 && notaNum <= 35){
        notaLetra = 'D';
    }else if(notaNum >= 36 && notaNum <= 60){
        notaLetra = 'C';
    }else if(notaNum >= 61 && notaNum <= 85){
        notaLetra = 'B';
    }else if(notaNum >= 86 && notaNum <= 100){
        notaLetra = 'A';
    }

    printf("%c\n", notaLetra);

    return 0;
}