# Model K build entry points
# Hardware simulation requires Icarus Verilog.
# Native reference build requires a C11 compiler.

test:
	iverilog -g2012 -o model_k_tb rtl/gates.sv rtl/adders.sv rtl/alu.sv rtl/registers.sv rtl/memory.sv rtl/cpu.sv rtl/model_k.sv tb/model_k_tb.sv
	vvp model_k_tb

compile:
	$(MAKE) -C compile

compile-test:
	$(MAKE) -C compile test

clean:
	rm -f model_k_tb
	$(MAKE) -C compile clean
