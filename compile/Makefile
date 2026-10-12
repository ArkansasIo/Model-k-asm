CC ?= cc
CFLAGS ?= -std=c11 -O2 -Wall -Wextra -Wpedantic
CPPFLAGS ?= -Iinclude
OUTPUT_EX ?= ../output/ex
TARGET := $(OUTPUT_EX)/model-k
QK_TARGET := $(OUTPUT_EX)/model_qk

all: $(TARGET) $(QK_TARGET)

$(OUTPUT_EX):
	mkdir -p $(OUTPUT_EX)

$(TARGET): src/mk.c src/model_k.c include/model_k.h | $(OUTPUT_EX)
	$(CC) $(CFLAGS) $(CPPFLAGS) src/mk.c src/model_k.c -o $@

$(QK_TARGET): src/qk.c src/model_qk.c src/model_qk_database.c include/model_qk.h include/model_qk_database.h | $(OUTPUT_EX)
	$(CC) $(CFLAGS) $(CPPFLAGS) src/qk.c src/model_qk.c src/model_qk_database.c -o $@

test: all
	./$(TARGET) version
	./$(TARGET) add20 0xFFFFF 1
	./$(TARGET) status
	./$(QK_TARGET) version
	./$(QK_TARGET) add64 0xFFFFFFFFFFFFFFFF 1

clean:
	rm -f $(TARGET) $(QK_TARGET)
