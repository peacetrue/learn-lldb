/**
 * 此程序用于演示可执行文件的日志。
 */
#include <stdio.h>
#include <stdlib.h>

long resolveArg(int argc, char **argv, long index, int defaults) {
    return argc >= index + 1 ? strtol(argv[index], NULL, 10) : defaults;
}

/**
* 主函数。
*
* @param argc 参数数目
* @param argv 参数指针。
*  <p/> argv[0]：程序路径
*  <p/> argv[1]：日志条数
*  @return 退出码
*/
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; ++i) {
        printf("argv[%i]: %s\n", i, argv[i]);
    }

    long logCount = resolveArg(argc, argv, 1, 2);
    for (int i = 0; i < logCount; ++i) {
        printf("log-%i\n", i);
    }
}
