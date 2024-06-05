#include <stdio.h>

int main(){
    unsigned int counter;

    scanf("%u", &counter);

    unsigned int game_board[counter];

    for(int i = 0; i < counter; i++){
        scanf("%u", &game_board[i]);
        
    }

    unsigned int result_game[counter];

    for(int j = 0; j < counter; j++){

        if(j == 0){
            result_game[j] = game_board[j] + game_board[j+1];
        }

        else if (j == counter -1 ){
            result_game[j] = game_board[j-1] + game_board[j];
        }

        else {
            result_game[j] = game_board[j-1] + game_board[j] + game_board[j+1];
        }

        printf("%u\n", result_game[j]);

    }

    return 0;
}