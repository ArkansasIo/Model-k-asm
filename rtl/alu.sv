module mk_alu(input logic [7:0] a,b, input logic [3:0] op,
output logic [7:0] y, output logic carry,zero,negative,overflow);
localparam OP_ADD=4'h0, OP_SUB=4'h1, OP_AND=4'h2, OP_OR=4'h3,
OP_XOR=4'h4, OP_NOT=4'h5, OP_SHL=4'h6, OP_SHR=4'h7,
OP_MUL=4'h8, OP_DIV=4'h9, OP_CMP=4'hA, OP_XNOR=4'hB,
OP_NAND=4'hC, OP_NOR=4'hD, OP_PASS=4'hE;
logic [7:0] add_y,sub_y; logic add_c,sub_b; logic [15:0] mul_full;
mk_add8 ad(.a(a),.b(b),.cin(1'b0),.sum(add_y),.cout(add_c));
mk_sub8 su(.a(a),.b(b),.diff(sub_y),.borrow(sub_b));
assign mul_full=a*b;
always_comb begin
y=0; carry=0; overflow=0;
case(op)
OP_ADD: begin y=add_y; carry=add_c; overflow=(~(a[7]^b[7]))&(y[7]^a[7]); end
OP_SUB: begin y=sub_y; carry=~sub_b; overflow=(a[7]^b[7])&(y[7]^a[7]); end
OP_AND:y=a&b; OP_OR:y=a|b; OP_XOR:y=a^b; OP_NOT:y=~a;
OP_SHL: begin y=a<<b[2:0]; if(b[2:0]!=0) carry=a[8-b[2:0]]; end
OP_SHR: begin y=a>>b[2:0]; if(b[2:0]!=0) carry=a[b[2:0]-1]; end
OP_MUL: begin y=mul_full[7:0]; carry=|mul_full[15:8]; end
OP_DIV: y=(b==0)?8'hFF:a/b;
OP_CMP:y=(a==b)?8'h00:((a<b)?8'hFF:8'h01);
OP_XNOR:y=~(a^b); OP_NAND:y=~(a&b); OP_NOR:y=~(a|b); OP_PASS:y=a;
default:y=0;
endcase
end
assign zero=(y==0); assign negative=y[7];
endmodule
