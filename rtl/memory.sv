// Byte-addressed memory. Each record occupies 20 consecutive bytes.
module mk_record_memory #(parameter integer RECORDS=256)(
input logic clk,we,input logic [15:0] addr,input logic [7:0] wdata,output logic [7:0] rdata);
localparam integer BYTES=RECORDS*20;
logic [7:0] mem[0:BYTES-1];
always_ff @(posedge clk) if(we && addr<BYTES) mem[addr]<=wdata;
always_comb if(addr<BYTES) rdata=mem[addr]; else rdata=8'hFF;
endmodule
