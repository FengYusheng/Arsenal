#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void version(void) {
    printf("Redis server v=%s bit=%d\n",
           "0.0.1",
           sizeof(long) == 4 ? 32 : 64
           );

    exit(0);
}


void usage(void) {
    fprintf(stderr, "Usage: ./redis-server [/path/to/redis.conf] [options]\n");
    fprintf(stderr, "       ./redis-server - (read config from stdin)\n");
    fprintf(stderr, "       ./redis-server -v or --version\n");
    fprintf(stderr, "       ./redis-server -h or --help\n");
    fprintf(stderr,"        ./redis-server --test-memory <megabytes>\n\n");
    fprintf(stderr, "Examples:\n");
    fprintf(stderr,"        ./redis-server (run the server with default conf)\n");
    fprintf(stderr,"        ./redis-server /etc/redis/6379.conf\n");
    fprintf(stderr,"        ./redis-server --port 7777\n");
    fprintf(stderr,"        ./redis-server /etc/myredis.conf --loglevel verbose\n\n");
    fprintf(stderr,"Sentinel mode:\n");
    fprintf(stderr,"        ./redis-server /etc/sentinel.conf --sentinel\n");
    exit(1);
}


int main(int argc, char *argv[])
{
    /*TODO: initialize the running environment*/

    /*Parse the command options*/
    if (argc >= 2) {
        if (strcmp(argv[1], "-v") == 0 ||
            strcmp(argv[1], "--version") == 0) version();
        if (strcmp(argv[1], "-h") == 0 ||
            strcmp(argv[1], "--help") == 0) usage();
    }
    return 0;
}
