%.o: %.cpp
	gcc -O2 -c $<

hello: hello.o main.o hook.o
	gcc -o $@ -Wl,--wrap="_ZN5Hello9callHelloEv" $^
all: hello
