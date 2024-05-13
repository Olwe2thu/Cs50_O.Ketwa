#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    //declare /initialize variables
    char letters[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    int scores[] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    int player1Score = 0, player2Score = 0;
    string player1Guess, player2Guess;
    int length= sizeof(letters) / sizeof(letters[0]);

    //prompting user input
    player1Guess = get_string("Player 1: ");
    player2Guess = get_string("Player 2: ");

    //CHECK Player 1 && looping through player guess
    for( int i = 0; i < strlen(player1Guess);i++)
    {
        //looping through array
        for(int j = 0; j < length; j++)
        {
            if(letters[j] == toupper(player1Guess[i]))
            {
                player1Score += scores[j];
            }
        }
    }

    //CHECK Player 2 && loop through
    for( int i = 0; i < strlen(player2Guess);i++)
    {
        for(int j = 0; j<length; j++)
        {
            if(letters[j] == toupper(player2Guess[i]))
            {
                player2Score += scores[j];
            }
        }
    }

    //COMPARE Scores && CHECK for winner
    if( player1Score > player2Score)
    {
        printf("Player 1 Wins!\n");
    }
    else if( player2Score > player1Score )
    {
        printf("Player 2 Wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
