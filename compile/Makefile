CC ?= cc
CFLAGS ?= -std=c11 -O2 -Wall -Wextra -Wpedantic
CPPFLAGS ?= -Iinclude
TARGET := build/model-k

all: $(TARGET)

$(TARGET): src/mk.c src/model_k.c include/model_k.h
	mkdir -p build
	$(CC) $(CFLAGS) $(CPPFLAGS) src/mk.c src/model_k.c -o $@

test: $(TARGET)
	./$(TARGET) version
	./$(TARGET) add20 0xFFFFF 1
	./$(TARGET) status

clean:
	rm -rf build/*
