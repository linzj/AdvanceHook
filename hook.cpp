#include <stdio.h>
#include "hello.h"

void nimabi(void (*origin)(Hello*), Hello* h)
{
    printf("nimabi before call Hello::callHello\n");
    h->setNum(1234);
    origin(h);
    printf("nimabi after call Hello::callHello\n");
}
