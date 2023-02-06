//////////////////////////////////////////
//  Functionality: A two-stage clock divider (Frequency is divided by 4)
//                 This is to test the clock generated locally by a LUT/FF
//  Author:        Xifan Tang
////////////////////////////////////////
`timescale 1ns / 1ps

module clk_divider(rst,clk_i, clk_o);

input wire rst;
input wire clk_i;
output reg clk_o;

reg  int_clk;


always @(posedge clk_i or posedge rst) begin
 if(rst)begin
 int_clk = 0; 
 clk_o = 0;
 end
 else begin int_clk = ~int_clk; end
end

always @(posedge int_clk or posedge rst) begin
if(rst)begin
 int_clk = 0; 
 clk_o = 0;
end
else begin  clk_o = ~clk_o; end
end


endmodule
