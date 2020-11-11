// gcc -Wall -fno-stack-protector -no-pie leap2victory.c -o leap2victory
#include <stdio.h>
#include <unistd.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int main() {
    char buf[32];

    printf("This program is unhackable! Don't even try it!\n");
    gets(buf);
}

void win() {
    execve("/bin/sh", 0, 0);
}
