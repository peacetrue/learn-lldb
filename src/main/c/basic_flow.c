/** 演示 LLDB 基本使用流程。 */
#include <printf.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

long resolveArg(int argc, char **argv, long index, int defaults) {
    return argc >= index + 1 ? strtol(argv[index], NULL, 10) : defaults;
}

void *thread_func(void *arg) {
    pthread_setname_np("thread-2");
    sleep((long) arg);
    return arg;
}

/**
 * 主函数。
 *
 * @param argc 参数数目
 * @param argv 参数指针。
 *  <p/> argv[0]：程序路径
 *  <p/> argv[1]：子线程睡眠秒数，默认为 10
 *  @return 退出码
 */
int main(int argc, char *argv[]) {
    long seconds = resolveArg(argc, argv, 1, 10);
    printf("$ lldb %s\n", argv[0]);
    printf("(lldb) target create %s\n", argv[0]);
    printf("(lldb) target list\n");
    printf("(lldb) b main\n");
    printf("(lldb) r\n");

    pthread_t thread;
    pthread_create(&thread, NULL, thread_func, (void *) seconds);

    printf("(lldb) thread list\n");
    printf("(lldb) thread info\n");
    printf("(lldb) thread select 1\n");

    printf("(lldb) frame info\n");
    printf("(lldb) bt\n");
    printf("(lldb) frame select 1\n");

    printf("(lldb) re read rsp\n");
    printf("(lldb) x/16g $rsp\n");
    printf("(lldb) p argv[0]\n");
    printf("(lldb) p (int)strlen(argv[0])\n");
}


