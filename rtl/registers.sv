module mk_register8(input logic clk,reset,we,input logic [7:0] d,output logic [7:0] q);
always_ff @(posedge clk) begin if(reset) q<=0; else if(we) q<=d; end
endmodule
module mk_flags(input logic clk,reset,we,input logic carry,zero,negative,overflow,output logic C,Z,N,V);
always_ff @(posedge clk) begin
if(reset) begin C<=0;Z<=0;N<=0;V<=0;end
else if(we) begin C<=carry;Z<=zero;N<=negative;V<=overflow;end
end
endmodule
