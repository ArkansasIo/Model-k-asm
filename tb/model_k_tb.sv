module model_k_tb;
logic a,b; logic [2:0] k2;
mk_k2_adder dut(.a({1'b0,a}),.b({1'b0,b}),.cin(1'b0),.sum(k2));
initial begin
for(int i=0;i<2;i++) for(int j=0;j<2;j++) begin
a=i; b=j; #1; assert(k2==i+j) else $fatal("K2 failed");
end
$display("K2 adder PASS"); $finish;
end
endmodule
