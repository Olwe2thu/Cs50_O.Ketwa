#include <stdio.h>
#include <cs50.h>

void hello(void);
int main(void){
    hello();
}

void hello(void){
    string name="";

     name = get_string ("What is your name? ");

        printf("hello, %s\n",name);
}
