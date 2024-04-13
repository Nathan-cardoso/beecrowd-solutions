#include <stdio.h>
 
int main() {
    int a, b;
    while((a < 1 || a > 13) || (b < 1 || b > 13)){
    scanf("%d%d", &a,&b);
    }
    
    int c;

    if(a == b){
        
        c = a;
    }
    else if(a > b){
        c = a;
    }
    else if(a < b){
        c = b;
    }
    else{
        c = 13;
    }

    printf("%d\n",c);
 
    return 0;
}