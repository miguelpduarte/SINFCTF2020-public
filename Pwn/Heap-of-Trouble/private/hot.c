// gcc -Wall hot.c -o hot

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

char * registration;
char * voucher;

int main(void) {
    printf("Welcome to my first heap program! I learned how to use malloc and free for the first time here!\n");
    printf("With this program you can register to win flags in a raffle!\n");

    char option;
    char clear_buffer;
    char input_buf[256];
    size_t str_len;

    do {
	printf("\n1 - Register for the contest\n2 - Display your registration\n3 - Delete your registration (irreversible, RGPD...)\n4 - Add voucher\n5 - Win raffle\n\nPlease pick the desired option: ");
	fflush(stdout);
	option = getchar();
	do {
	    clear_buffer = getchar();
	    // Clear the newline that might be entered too
	    if (clear_buffer == '\n')  break;
	    // While not EOF
	} while(clear_buffer != -1);

	switch (option) {
	    case '1':
		// Register
		registration = malloc(72);
		printf("\nName: ");
		fflush(stdout);
		fgets(input_buf, 256, stdin);
		strncpy(registration, input_buf, 30);
		// Covering for strncpy potential lack of \0
		str_len = strlen(registration);
		if (str_len < 31) {
		    registration[str_len - 1] = '\0';
		} else {
		    registration[31] = '\0';
		}
		
		printf("\nEmail: ");
		fflush(stdout);
		fgets(input_buf, 256, stdin);
		strncpy(registration + 32, input_buf, 30);
		// Covering for strncpy potential lack of \0
		str_len = strlen(registration + 32);
		if (str_len < 31) {
		    registration[str_len + 31] = '\0';
		} else {
		    registration[63] = '\0';
		}

		printf("\nThanks for the registration. Your ticket number is %d\n", registration);
		break;
	    case '2':
		// Display
		if (registration == NULL) {
		    printf("\nYou haven't registered for the raffle yet!\n");
		} else {
		    printf("\n===== Ticket #%d =====\nName: %s\nEmail: %s\nChances to win: %d\n\n",
			    registration, registration, registration + 32, *(int *)(registration + 64));
		}
		break;
	    case '3':
		// Delete
		if (registration == NULL) {
		    printf("\nNo registration found to delete.\n");
		} else {
		    free(registration);
		    printf("\nRegistration deleted successfully!!\n");
		}
		break;
	    case '4':
		// Add voucher
		printf("\nPlease enter voucher: ");
		fflush(stdout);
		fgets(input_buf, 256, stdin);
		voucher = strdup(input_buf);
		printf("\nThanks! Voucher submission ID: %d\n", voucher);
		break;
	    case '5':
		// Flag
		/* printf("\nreg:%d", registration); */
		/* printf("\nstr:%s", registration); */
		/* printf("\nsol:%s", registration+64); */
		/* printf("\n### test: %x", *(registration + 64)); */
		/* printf("\n### test: %x", *(registration + 65)); */
		/* printf("\n### test: %x", *(registration + 66)); */
		/* printf("\n### test: %x\n", *(registration + 67)); */
		if (registration == NULL || *(int *)(registration + 64) != 0x7a707a65) {
		    printf("\nYou haven't won yet! Try again!\n");
		} else {
		    system("/bin/cat flag.txt");
		}
		break;
	}
    } while(1);
}
