// Compile with stack canary but without PIE
// gcc -Wall -no-pie -fstack-protector coal_mine.c -o coal_mine
#include <stdio.h>
#include <stdlib.h>

#include <unistd.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int main() {
    char name[32];
    char what_to_mine[32];
    printf("Welcome to the Coal Mine!\nWhat's your name, fellow miner?\n");
    // This should be safe relative to BOF
    fgets(name, sizeof(name), stdin);
    printf("Thanks, ");
    printf(name);
    printf("\n");

    printf("\nAnd what will you be mining today?\n");
    gets(what_to_mine);
    printf("That's great! See you at the mine!\n");
}

void mine_diamonds() {
    // system("/bin/sh"); // Was inconsistent if stack got borked (via EBP overwrite)
    execve("/bin/sh", NULL, NULL);
}
