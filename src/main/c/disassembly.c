/**
 * 参考 disassembly.mk。
 */
#include <printf.h>

void step() {
    printf("source debug\n");
}

void step_i() {
    printf("disassembly debug\n");
}

int main() {
    step();
    step_i();
}
