#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "model_qk.h"

static void usage(const char *p) {
    puts("Model QK native reference");
    printf("Usage: %s version | add64 A B | sub64 A B | checksum\n", p);
}

int main(int argc, char **argv) {
    if (argc < 2) { usage(argv[0]); return 1; }
    if (!strcmp(argv[1], "version")) {
        puts("Model QK 2.0.0 native reference");
        return 0;
    }
    if ((!strcmp(argv[1], "add64") || !strcmp(argv[1], "sub64")) && argc == 4) {
        uint64_t a = strtoull(argv[2], NULL, 0);
        uint64_t b = strtoull(argv[3], NULL, 0);
        uint64_t r = !strcmp(argv[1], "add64") ? qk64_add(a, b) : qk64_sub(a, b);
        printf("0x%016llX\n", (unsigned long long)r);
        return 0;
    }
    usage(argv[0]);
    return 1;
}
