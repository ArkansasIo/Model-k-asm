module mk_cpu(input logic clk,reset,input logic [15:0] instr_in,output logic [7:0] result_out,pc_out);
localparam OP_ADD=4'h0, OP_SUB=4'h1, OP_AND=4'h2, OP_OR=4'h3, OP_XOR=4'h4,
OP_NOT=4'h5, OP_SHL=4'h6, OP_SHR=4'h7, OP_MUL=4'h8, OP_DIV=4'h9,
OP_CMP=4'hA, OP_XNOR=4'hB, OP_NAND=4'hC, OP_NOR=4'hD, OP_MOVI=4'hE, OP_HALT=4'hF;
logic [7:0] r[0:7],pc; logic halted; logic [3:0] opcode,rd,rs,fn;
logic [7:0] alu_y,b_operand; logic c,z,n,v;
assign opcode=instr_in[15:12]; assign rd=instr_in[11:8]; assign rs=instr_in[7:4]; assign fn=instr_in[3:0];
always_comb b_operand=(opcode==OP_MOVI)?{4'h0,fn}:r[rs];
mk_alu alu(.a(r[rd]),.b(b_operand),.op(opcode),.y(alu_y),.carry(c),.zero(z),.negative(n),.overflow(v));
always_ff @(posedge clk) begin
if(reset) begin pc<=0; halted<=0; for(int i=0;i<8;i++) r[i]<=0; end
else if(!halted) begin
case(opcode) OP_HALT:halted<=1; OP_MOVI:r[rd]<={4'h0,fn}; default:r[rd]<=alu_y; endcase
pc<=pc+1'b1;
end end
assign result_out=r[0]; assign pc_out=pc;
endmodule
