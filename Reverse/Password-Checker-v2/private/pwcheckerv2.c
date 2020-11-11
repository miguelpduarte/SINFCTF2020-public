// gcc -Wall pwcheckerv2.c -o pwcheckerv2
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int valid_password(char * input) {
    if (strlen(input) != 8) {
	return 0;
    }

    int sum = 0;

    for (int i = 0; i < 8; ++i) {
	sum += input[i];
    }

    // printf("sum: %d\n", sum);
    if (sum == 900) {
	return 1;
    }
    
    return 0;
}

void print_flag() {
    FILE * file = fopen("./flag.txt", "r");
    char c;
    if (file) {
	while ((c = getc(file)) != EOF) {
	    putchar(c);
	}
	fclose(file);
    }
}

int main(void) {
    // avestruz
    // avestrvy
    // ...
    char input[9];
    printf("What's the password?\n");
    
    // This should be safe relative to BOF
    fgets(input, sizeof(input), stdin);

    if (valid_password(input)) {
	print_flag();
    } else {
	printf("Sorry! Try again!\n");
    }
}
