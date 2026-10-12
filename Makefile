# Model QK — Aethernox Paradox Core build entry points
# Legacy RTL and native reference targets remain available.
# Compiled native executables are staged under output/ex/.

OUTPUT_EX := output/ex

test:
	iverilog -g2012 -o $(OUTPUT_EX)/model_k_tb rtl/gates.sv rtl/adders.sv rtl/alu.sv rtl/registers.sv rtl/memory.sv rtl/cpu.sv rtl/model_k.sv tb/model_k_tb.sv
	vvp $(OUTPUT_EX)/model_k_tb

compile:
	$(MAKE) -C compile

compile-test:
	$(MAKE) -C compile test

quantum-test:
	python -m unittest discover -s quantum/tests -p 'test_*.py' -v

quantum-procedural:
	python quantum/apps/procedural_generator.py --seed 20261011 --qubits 4 --depth 12 --algorithm variational

quantum-virtual:
	python quantum/apps/virtual_hardware.py --qubits 4 --shots 1024 --seed 20261011

clean:
	rm -rf $(OUTPUT_EX)
	$(MAKE) -C compile clean
