module mk_full_adder(input logic a,b,cin, output logic sum,cout);
logic x; assign x=a^b; assign sum=x^cin; assign cout=(a&b)|(cin&x);
endmodule
module mk_half_adder(input logic a,b, output logic sum,carry);
assign sum=a^b; assign carry=a&b;
endmodule
module mk_k2_adder(input logic [1:0] a,b, input logic cin, output logic [2:0] sum);
logic c0;
mk_full_adder fa0(.a(a[0]),.b(b[0]),.cin(cin),.sum(sum[0]),.cout(c0));
mk_full_adder fa1(.a(a[1]),.b(b[1]),.cin(c0),.sum(sum[1]),.cout(sum[2]));
endmodule
module mk_add8(input logic [7:0] a,b, input logic cin, output logic [7:0] sum, output logic cout);
logic [7:0] c;
mk_full_adder f0(a[0],b[0],cin,sum[0],c[0]);
mk_full_adder f1(a[1],b[1],c[0],sum[1],c[1]);
mk_full_adder f2(a[2],b[2],c[1],sum[2],c[2]);
mk_full_adder f3(a[3],b[3],c[2],sum[3],c[3]);
mk_full_adder f4(a[4],b[4],c[3],sum[4],c[4]);
mk_full_adder f5(a[5],b[5],c[4],sum[5],c[5]);
mk_full_adder f6(a[6],b[6],c[5],sum[6],c[6]);
mk_full_adder f7(a[7],b[7],c[6],sum[7],cout);
endmodule
module mk_sub8(input logic [7:0] a,b, output logic [7:0] diff, output logic borrow);
logic c; mk_add8 ad(.a(a),.b(~b),.cin(1'b1),.sum(diff),.cout(c)); assign borrow=~c;
endmodule
