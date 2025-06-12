#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *tape;
int head = 0;
char state[4] = "q0";

int is_final_state() {
    return strcmp(state, "qf") == 0;
}

int step() {
    int len = strlen(tape);
    if (head >= len) {
        tape = realloc(tape, len + 2);
        tape[len] = '_';
        tape[len + 1] = '\0';
    } else if (head < 0) {
        tape = realloc(tape, len + 2);
        memmove(tape + 1, tape, len + 1);
        tape[0] = '_';
        head = 0;
    }

    char symbol = tape[head];

    if (strcmp(state, "q0") == 0 && symbol == 'a') { tape[head] = '_'; head++; strcpy(state, "q1"); return 1; }
    if (strcmp(state, "q0") == 0 && symbol == 'b') { tape[head] = '_'; head++; strcpy(state, "q2"); return 1; }
    if (strcmp(state, "q0") == 0 && symbol == '_') { head++; strcpy(state, "qf"); return 1; }

    if (strcmp(state, "q1") == 0 && symbol == 'a') { head++; return 1; }
    if (strcmp(state, "q1") == 0 && symbol == 'b') { head++; return 1; }
    if (strcmp(state, "q1") == 0 && symbol == '_') { head--; strcpy(state, "q3"); return 1; }
    if (strcmp(state, "q3") == 0 && symbol == 'a') { tape[head] = '_'; head--; strcpy(state, "q4"); return 1; }
    if (strcmp(state, "q3") == 0 && symbol == '_') { head++; strcpy(state, "qf"); return 1; }

    if (strcmp(state, "q2") == 0 && symbol == 'a') { head++; return 1; }
    if (strcmp(state, "q2") == 0 && symbol == 'b') { head++; return 1; }
    if (strcmp(state, "q2") == 0 && symbol == '_') { head--; strcpy(state, "q5"); return 1; }
    if (strcmp(state, "q5") == 0 && symbol == 'b') { tape[head] = '_'; head--; strcpy(state, "q4"); return 1; }
    if (strcmp(state, "q5") == 0 && symbol == '_') { head++; strcpy(state, "qf"); return 1; }

    if (strcmp(state, "q4") == 0 && symbol == 'a') { head--; return 1; }
    if (strcmp(state, "q4") == 0 && symbol == 'b') { head--; return 1; }
    if (strcmp(state, "q4") == 0 && symbol == '_') { head++; strcpy(state, "q0"); return 1; }

    return 0;
}

int run() {
    while (!is_final_state()) {
        if (!step()) break;
    }
    return is_final_state();
}

int main() {
    char input[100];
    printf("Ingrese una cadena con 'a' y 'b': ");
    scanf("%s", input);

    for (int i = 0; input[i]; ++i) {
        if (input[i] != 'a' && input[i] != 'b') {
            printf("Solo se permiten las letras 'a' y 'b'\n");
            return 1;
        }
    }

    tape = malloc(strlen(input) + 2);
    strcpy(tape, input);
    if (run()) {
        printf("Cadena aceptada (palíndromo)\n");
    } else {
        printf("Cadena rechazada\n");
    }

    free(tape);
    return 0;
}