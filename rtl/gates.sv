module mk_and(input logic a,b, output logic y); assign y = a & b; endmodule
module mk_or(input logic a,b, output logic y); assign y = a | b; endmodule
module mk_xor(input logic a,b, output logic y); assign y = a ^ b; endmodule
module mk_not(input logic a, output logic y); assign y = ~a; endmodule
module mk_nand(input logic a,b, output logic y); assign y = ~(a & b); endmodule
module mk_nor(input logic a,b, output logic y); assign y = ~(a | b); endmodule
module mk_xnor(input logic a,b, output logic y); assign y = ~(a ^ b); endmodule
module mk_gate_bank(input logic a,b, output logic and_y,or_y,xor_y,not_a,nand_y,nor_y,xnor_y);
assign and_y=a&b; assign or_y=a|b; assign xor_y=a^b; assign not_a=~a;
assign nand_y=~(a&b); assign nor_y=~(a|b); assign xnor_y=~(a^b);
endmodule
