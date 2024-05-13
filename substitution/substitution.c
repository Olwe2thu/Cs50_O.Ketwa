#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int args, string argv[])
{
    //checking if key is entered and is of valid length
    if(args != 2 || strlen(argv[1]) != 26  )
    {
        printf("Usage:  %s key\n", argv[0]);
        return 1;
    }
    string key = argv[1];

    //checking if key contains only letters without duplicates.
    for( int i = 0; i < strlen(key); i++)
    {
        int count=0;
        if(!isalpha(key[i]) )
        {
            printf("Key must contain only letters\n");
            return 1;
        }

            for(int k = 0; k < strlen(key); k++)
            {
                if(key[i] == key[k])
                {
                    count++;
                }

                if(count >1)
                {
                    printf("Key must not contain duplicates\n");
                    return 1;
                }
            }
    }

    //get user input and print output
    string text = get_string("Plaintext: ");
    printf("ciphertext: ");

    char cipher[strlen(text)];
    //encrypting the text
    for (int i = 0; i <= strlen(text); i++)
    {
        char c = text[i];
        if (isalpha(c))
        {
            //checking char cassing
            cipher[i] =(islower(c)) ?  tolower(key[c-'a']) : toupper(key[c-'A']);
        }
        else
        {
            cipher[i] = c;
        }
    }
    //print ciphered text
    printf("%s",cipher);
    printf("\n");
}

