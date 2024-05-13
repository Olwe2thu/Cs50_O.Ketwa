#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

//prototypes
bool only_digits(string key);
char rotate(char c, int key);
int main(int argc, string argv[])
{
    //evaluating if cmd line key is entered
    if(argc != 2)
    {
        printf("Usage:  %s key\n", argv[0]);
        return 1;
    }

    //parsing argv to variable & converting to int
    string arg = argv[1];
    int key = atoi(argv[1]);

    //checking if key contains only digits
    if(only_digits(arg) == false)
    {
        printf("Usage: %s key\n",argv[0]);
        return 1;
    }

    //prompting and getting user input && printing ciphertext
    string text = get_string("Plaintext: ");
    printf("ciphertext:");

    // looping through plaintext
    for(int i = 0; i < strlen(text); i++)
    {
        printf("%c", rotate(text[i], key));
    }
    printf("\n");
}

bool only_digits(string key)
{
    //check if key is valid(no letters || characters)
    for(int o = 0; o < strlen(key); o++)
    {
        if(!isdigit(key[o]))
        {
            return false;
        }
    }
    //check if key is in ranges 0-9/ 0-100 == check50..
    // int intKey = atoi(key);
    // return (intKey < 0 || intKey > 100) ? false :  true  ;
    return true;
}

char rotate(char c, int key)
{
     // looping through each single char in plaintext and rotating it by number of positions indicated by key
        if( isupper(c))
        {
            return (c - 65 + key) % 26 + 65;
        }
        else if(islower(c))
        {
            return (c - 97 + key) % 26 + 97;
        }
        else
        {
            return c;
        }
}
