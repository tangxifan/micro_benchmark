///////////////////////////////////////////
//  Functionality: 4-Clock 8-bit Pipelined Multiplier (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module mult_8_pipelined_4clk (
    input clk0,
    input clk1,
    input clk2,
    input clk3,
    input [7:0] a0,
    input [7:0] b0,
    input [7:0] a1,
    input [7:0] b1,
    input [7:0] a2,
    input [7:0] b2,
    input [7:0] a3,
    input [7:0] b3,
    output [15:0] p0,
    output [15:0] p1,
    output [15:0] p2,
    output [15:0] p3
);

    // Instantiate Multiplier 0
    mult_8_pipelined u_mult0 (
        .clk(clk0),
        .a(a0),
        .b(b0),
        .p(p0)
    );

    // Instantiate Multiplier 1
    mult_8_pipelined u_mult1 (
        .clk(clk1),
        .a(a1),
        .b(b1),
        .p(p1)
    );

    // Instantiate Multiplier 2
    mult_8_pipelined u_mult2 (
        .clk(clk2),
        .a(a2),
        .b(b2),
        .p(p2)
    );

    // Instantiate Multiplier 3
    mult_8_pipelined u_mult3 (
        .clk(clk3),
        .a(a3),
        .b(b3),
        .p(p3)
    );

endmodule
