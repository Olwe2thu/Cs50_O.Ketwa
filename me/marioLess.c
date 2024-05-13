#include <cs50.h>
#include <stdio.h>

void mario(void);

int main(void)
{

    mario();
}

void mario(void)
{
    int choice = 1, level;
    printf("Welcome to mario\n");

      level = get_int("Please select level from 1- 8:\t");
      printf("\n");

      while (level <= 0 || level > 8)
      {
        level = get_int("Please select level from 1-8:\t");
      }

        for (int i = 1; i <= level; i++)
        {
            for (int j = level; j > i; j--)
            {
                printf(" ");
            }
            for (int k = 1; k <= i; k++)
            {
                printf("#");
            }
            printf(" ");

        printf("\n");
    }
}
