///////////////////////////////////////////
//  Functionality: 8-Clock 8-bit Pipelined Multiplier (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module mult_8_pipelined_8clk (
    input clk0, input clk1, input clk2, input clk3,
    input clk4, input clk5, input clk6, input clk7,
    input [7:0] a0, input [7:0] b0,
    input [7:0] a1, input [7:0] b1,
    input [7:0] a2, input [7:0] b2,
    input [7:0] a3, input [7:0] b3,
    input [7:0] a4, input [7:0] b4,
    input [7:0] a5, input [7:0] b5,
    input [7:0] a6, input [7:0] b6,
    input [7:0] a7, input [7:0] b7,
    output [15:0] p0,
    output [15:0] p1,
    output [15:0] p2,
    output [15:0] p3,
    output [15:0] p4,
    output [15:0] p5,
    output [15:0] p6,
    output [15:0] p7
);

    // Instantiate Multipliers 0 to 7[cite: 3]
    mult_8_pipelined u_mult0 (.clk(clk0), .a(a0), .b(b0), .p(p0));
    mult_8_pipelined u_mult1 (.clk(clk1), .a(a1), .b(b1), .p(p1));
    mult_8_pipelined u_mult2 (.clk(clk2), .a(a2), .b(b2), .p(p2));
    mult_8_pipelined u_mult3 (.clk(clk3), .a(a3), .b(b3), .p(p3));
    mult_8_pipelined u_mult4 (.clk(clk4), .a(a4), .b(b4), .p(p4));
    mult_8_pipelined u_mult5 (.clk(clk5), .a(a5), .b(b5), .p(p5));
    mult_8_pipelined u_mult6 (.clk(clk6), .a(a6), .b(b6), .p(p6));
    mult_8_pipelined u_mult7 (.clk(clk7), .a(a7), .b(b7), .p(p7));

endmodule
