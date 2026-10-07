///////////////////////////////////////////
// Functionality: 4-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_4clk (
    input [3:0] clk,
    input [31:0] a,
    input [31:0] b,
    output [63:0] p
);

    mult_8_pipelined_Nclk #(.N(4)) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
