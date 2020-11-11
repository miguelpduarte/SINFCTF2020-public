// Compile with executable stack and 32 bit (to be related with the second part)
// gcc -Wall -m32 -z execstack -fno-stack-protector shellcoat.c -o shellcoat

#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int main(void) {
    char coat[256];

    printf("I think I left my coat around %p\n", coat);

    gets(coat);
}
