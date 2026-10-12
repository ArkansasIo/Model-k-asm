module model_k_quantum_interface #(parameter int MAX_QUBITS=16)(input logic clk,input logic rst_n,input logic cmd_valid,input logic [7:0] cmd,input logic [7:0] q0,input logic [7:0] q1,input logic [31:0] angle,output logic busy,output logic result_valid,output logic [31:0] result);
always_ff @(posedge clk or negedge rst_n) begin
 if(!rst_n) begin busy<=0; result_valid<=0; result<='0; end
 else begin result_valid<=0; if(cmd_valid) busy<=1; end
end
endmodule
