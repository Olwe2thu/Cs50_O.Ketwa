#include <stdio.h>
#include <cs50.h>
#include <string.h>

int visa(long num);
int mastercard(long num);
int americanExpress(long num);

int main(int args, string argv[])
{
    //declaring/initializing variables used
    long num ;
    int count = 0;
    int digit;
    long modulus = 10;
    long division = 1;
    int sumDoubles = 0;
    int sum = 0;

     //get and prompt input
    do
    {
         num = get_long("Number:\t");
    }
    while( num <= 0 );

    //counter for input stream
    while (count < 16)
    {
        //get last digitit in stream
        digit = (num % modulus) / division;

        //checks whether digitit should be miltiplied or added
        if (count % 2 == 1)
        {
            digit *= 2;
            if (digit >= 10)
            {
                sumDoubles += digit / 10;
                sumDoubles += digit % 10;
            }
            else
            {
                sumDoubles += digit;
            }
        }
        else
        {
            sum += digit;
        }

        //moving to the next digitit in stream
        modulus *= 10;
        division *= 10;

        count++;
    }

    int total = sum + sumDoubles;
    int finTotal = total % 10;

    //determine card type
    if (visa(num) == 4 && finTotal == 0)
    {
        printf("VISA\n");
    }
    else if ((americanExpress(num) == 34 || americanExpress(num) == 37) && finTotal == 0)
    {
        printf("AMEX\n");
    }
    else if ((mastercard(num) >= 51 && mastercard(num) <= 55) && finTotal == 0)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

int visa(long num)
{
    while (num >= 10)
    {
        num /= 10;
    }
    return num;
}

int mastercard(long num)
{
    while (num >= 100)
    {
        num /= 10;
    }
    return num;
}

int americanExpress(long num)
{
    while (num >= 100)
    {
        num /= 10;
    }
    return num;
}
