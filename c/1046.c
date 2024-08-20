#include <stdio.h>

int cont_time(int inp,int out);

int main(){

    int time_init, time_final;

    scanf("%d %d", &time_init, &time_final);

    if((time_init < 0 || time_init > 23) || (time_final < 0 || time_final > 23)){
        return -1;
    }

    printf("O JOGO DUROU %d HORA(S)\n", cont_time(time_init, time_final));

    return 0;
}

int cont_time(int inp,int out){
    int count = 0;

    if(inp == out){
        return 24;
    }

    while(inp != out){

        if(inp > out){

            count++;

            inp++;

            if(inp > 23){
                inp = 0;
            }

        }
        else if(inp < out){
            count++;

            inp++;
        }
        

    }

    return count;

}