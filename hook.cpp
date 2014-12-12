#include <stdio.h>
#include "hello.h"
extern "C" {
    void __wrap__ZN5Hello9callHelloEv(Hello*);
    void __real__ZN5Hello9callHelloEv(Hello*);
}
void __wrap__ZN5Hello9callHelloEv(Hello* h)
{
    printf("__wrap__ZN5Hello9callHelloEv before call Hello::callHello\n");
    h->setNum(1234);
    __real__ZN5Hello9callHelloEv(h);
    printf("__wrap__ZN5Hello9callHelloEv after call Hello::callHello\n");
}
