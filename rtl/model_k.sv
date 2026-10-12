module model_k(input logic clk,reset,input logic [15:0] instruction,output logic [7:0] result,pc);
mk_cpu cpu(.clk(clk),.reset(reset),.instr_in(instruction),.result_out(result),.pc_out(pc));
endmodule
