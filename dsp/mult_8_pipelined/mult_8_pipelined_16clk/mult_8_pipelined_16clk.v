///////////////////////////////////////////
//  Functionality: 16-Clock 8-bit Pipelined Multiplier (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module mult_8_pipelined_16clk (
    input clk0,  input clk1,  input clk2,  input clk3,
    input clk4,  input clk5,  input clk6,  input clk7,
    input clk8,  input clk9,  input clk10, input clk11,
    input clk12, input clk13, input clk14, input clk15,
    input [7:0] a0,  input [7:0] b0,
    input [7:0] a1,  input [7:0] b1,
    input [7:0] a2,  input [7:0] b2,
    input [7:0] a3,  input [7:0] b3,
    input [7:0] a4,  input [7:0] b4,
    input [7:0] a5,  input [7:0] b5,
    input [7:0] a6,  input [7:0] b6,
    input [7:0] a7,  input [7:0] b7,
    input [7:0] a8,  input [7:0] b8,
    input [7:0] a9,  input [7:0] b9,
    input [7:0] a10, input [7:0] b10,
    input [7:0] a11, input [7:0] b11,
    input [7:0] a12, input [7:0] b12,
    input [7:0] a13, input [7:0] b13,
    input [7:0] a14, input [7:0] b14,
    input [7:0] a15, input [7:0] b15,
    output [15:0] p0,  output [15:0] p1,  output [15:0] p2,  output [15:0] p3,
    output [15:0] p4,  output [15:0] p5,  output [15:0] p6,  output [15:0] p7,
    output [15:0] p8,  output [15:0] p9,  output [15:0] p10, output [15:0] p11,
    output [15:0] p12, output [15:0] p13, output [15:0] p14, output [15:0] p15
);

    // Instantiate Multipliers 0 to 15
    mult_8_pipelined u_mult0  (.clk(clk0),  .a(a0),  .b(b0),  .p(p0));
    mult_8_pipelined u_mult1  (.clk(clk1),  .a(a1),  .b(b1),  .p(p1));
    mult_8_pipelined u_mult2  (.clk(clk2),  .a(a2),  .b(b2),  .p(p2));
    mult_8_pipelined u_mult3  (.clk(clk3),  .a(a3),  .b(b3),  .p(p3));
    mult_8_pipelined u_mult4  (.clk(clk4),  .a(a4),  .b(b4),  .p(p4));
    mult_8_pipelined u_mult5  (.clk(clk5),  .a(a5),  .b(b5),  .p(p5));
    mult_8_pipelined u_mult6  (.clk(clk6),  .a(a6),  .b(b6),  .p(p6));
    mult_8_pipelined u_mult7  (.clk(clk7),  .a(a7),  .b(b7),  .p(p7));
    mult_8_pipelined u_mult8  (.clk(clk8),  .a(a8),  .b(b8),  .p(p8));
    mult_8_pipelined u_mult9  (.clk(clk9),  .a(a9),  .b(b9),  .p(p9));
    mult_8_pipelined u_mult10 (.clk(clk10), .a(a10), .b(b10), .p(p10));
    mult_8_pipelined u_mult11 (.clk(clk11), .a(a11), .b(b11), .p(p11));
    mult_8_pipelined u_mult12 (.clk(clk12), .a(a12), .b(b12), .p(p12));
    mult_8_pipelined u_mult13 (.clk(clk13), .a(a13), .b(b13), .p(p13));
    mult_8_pipelined u_mult14 (.clk(clk14), .a(a14), .b(b14), .p(p14));
    mult_8_pipelined u_mult15 (.clk(clk15), .a(a15), .b(b15), .p(p15));

endmodule
