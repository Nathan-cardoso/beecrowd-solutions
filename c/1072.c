#include <stdio.h>

int main(){
    int n;
    scanf("%i", &n);

    int v[n];
    int in = 0, out = 0;
    for(int i = 0; i < n; i++){
        scanf("%i", i + v);

        if(v[i] >= 10 && v[i] <= 20){
            in++;
        }else{
            out++;
        }
    }

    printf("%i in\n",in);
    printf("%i out\n",out);

    
}