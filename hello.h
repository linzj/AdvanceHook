#ifndef HELLO_H
#define HELLO_H
#pragma once

class Hello
{
public:
    explicit Hello(int num);
    inline void setNum(int num) { m_num = num; }
    void callHello();
private:
    int m_num;
};
#endif /* HELLO_H */
