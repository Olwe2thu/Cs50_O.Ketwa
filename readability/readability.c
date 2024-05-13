#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//method prototypes
int letterCount(string text);
int wordCount(string text);
int sentenceCount(string text);
void printIndex(int index);

int main(int argc,string argv[])
{
    //prompting user input
    string text = get_string("Text: ");

    //calculating the grade index using formula
    float letterAvg = (float)letterCount(text) / (float)wordCount(text) * 100;
    float sentenceAvg= (float)(sentenceCount(text) || 1) / (float)wordCount(text) * 100;
    int index = round(0.0588 * letterAvg - 0.296 * sentenceAvg - 15.8);

    //checking text grade index
    printIndex(index);
}

void printIndex(int index)
{
    if(index <= 0)
    {
        printf("Before Grade 1\n");
    }
    else if( index <= 16)
    {
        printf("Grade %i\n",index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}
//counting letters in text
int letterCount(string text)
{
    float lCount = 0;

    for(int i = 0; i <strlen(text); i++)
    {
        if(isalpha(text[i]))
        {
            lCount++;
        }
    }
    return lCount;
}
//counting words in text
int wordCount(string text)
{
    float wCount = 0;

     for(int i = 0; i <strlen(text); i++)
     {
        if(isspace(text[i]))
        {
            wCount++;
        }
     }
     return wCount +1 ;
}
//counting sentences in text
int sentenceCount(string text)
{
    int sCount = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        if(text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sCount++;
        }
    }
    return sCount ;
}




