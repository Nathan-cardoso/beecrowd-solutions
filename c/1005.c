#include <stdio.h>

double average(double a, double b);


int main(){
    double note_one, note_two;

    scanf("%lf %lf", &note_one, &note_two);

    printf("MEDIA = %.5lf\n", average(note_one, note_two));

    return 0;
}


double average(double a, double b){
    return ((a * 3.5) + (b * 7.5))/ 11;
}