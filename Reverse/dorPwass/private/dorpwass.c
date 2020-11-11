// gcc -Wall dorpwass.c -o dorpwass
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int valid_password(char * input) {
    if (strlen(input) != 32) {
	return 0;
    }

    if (
	input[13] == 'u' &&
	input[0] == 'w' &&
	input[27] == 's' &&
	input[25] == 'a' &&
	input[22] == 'l' &&
	input[16] == 'r' &&
	input[28] == 'w' &&
	input[14] == 'n' &&
	input[4] == 'a' &&
	input[11] == 'm' &&
	input[10] == 'o' &&
	input[17] == 'e' &&
	input[18] == 'a' &&
	input[19] == 'k' &&
	input[1] == 'h' &&
	input[20] == 'a' &&
	input[5] == 'n' &&
	input[15] == 'b' &&
	input[23] == 'e' &&
	input[21] == 'b' &&
	input[3] == 't' &&
	input[6] == 'a' &&
	input[7] == 'w' &&
	input[8] == 'e' &&
	input[26] == 's' &&
	input[24] == 'p' &&
	input[12] == 'e' &&
	input[29] == 'o' &&
	input[2] == 'a' &&
	input[30] == 'r' &&
	input[9] == 's' &&
	input[31] == 'd'
    ) {
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
    // whatanawesomeunbreakablepassword
    char input[33];
    printf("What's the password?\n");
    
    // This should be safe relative to BOF
    fgets(input, sizeof(input), stdin);

    if (valid_password(input)) {
	print_flag();
    } else {
	printf("Sorry! Try again!\n");
    }
}
