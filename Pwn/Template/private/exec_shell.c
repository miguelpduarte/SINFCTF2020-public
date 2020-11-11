#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int main(void) {
    printf("Here you go, a free shell!\n");
    system("/bin/sh");
}
