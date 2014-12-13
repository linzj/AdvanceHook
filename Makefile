%.o: %.cpp
	gcc -O2 -c $<

libhello.a: hello.o
	ar crs $@ $^

libhook.a: hook.o
	ar crs $@ $^

hello: hello.o main.o hook.o
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $^

hello2: main.o hook.o libhello.a
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $(filter %.o, $^) -L. -lhello
hello3: main.o hello.o libhook.a
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $(filter %.o, $^) -L. -lhook

.PHONY: all
all: hello hello2 hello3
