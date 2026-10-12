# Requires Icarus Verilog
test:
	iverilog -g2012 -o model_k_tb rtl/gates.sv rtl/adders.sv rtl/alu.sv rtl/registers.sv rtl/memory.sv rtl/cpu.sv rtl/model_k.sv tb/model_k_tb.sv
	vvp model_k_tb

clean:
	rm -f model_k_tb
