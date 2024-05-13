#include <cs50.h>
#include <stdio.h>

//declare constant variables
#define QUARTERS 25
#define DIMES 10
#define NICKELS 5
#define PENNIES 1

int main(void)
{
    int nCoins = 0, change, quarters=0,dimes=0,nickels=0,pennies=0;


    //prompt & get user input
    do
    {
        change = get_int("Change owed:\t ");
    }
    while (change <= 0);
    printf("\n");

    //calculate coins to be dispensed
    while (change > 0)
    {
        if (change >= QUARTERS)
        {
            change -= QUARTERS;
            nCoins++;
        }
        else if (change >= DIMES)
        {
            change -= DIMES;
            nCoins++;
        }
        else if (change >= NICKELS)
        {
            change -= NICKELS;
            nCoins++;
        }
        else
        {
            change-=1;
            nCoins++;
        }
    }
    printf("Quarters%i\n", quarters);
    printf("Nickels%i\n", nickels);
    printf("Dimes: %i\n", dimes);
    printf("Pennies: %i\n", pennies);


}
