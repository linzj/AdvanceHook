.PHONY: all
all: hello hello2 hello3
%.o: %.cpp
	gcc -O2 -c $<

%.o: %.c
	gcc -O2 -c $<

hook_output.c: hook_desc generator.py
	python generator.py

libhello.a: hello.o
	ar crs $@ $^

libhook.a: hook.o hook_output.o
	ar crs $@ $^

hello: hello.o main.o hook.o hook_output.o
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $^

hello2: main.o hook.o libhello.a hook_output.o
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $(filter %.o, $^) -L. -lhello
hello3: main.o hello.o libhook.a
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $(filter %.o, $^) -L. -lhook

