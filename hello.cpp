#include <stdio.h>
#include "hello.h"

Hello::Hello(int num) : m_num (num) {}
void Hello::callHello()
{
    printf("Hello::callHello: m_num = %d\n", m_num);
}
