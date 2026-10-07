///////////////////////////////////////////
// Functionality: 32-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_32clk (
    input [31:0] clk,
    input [255:0] a,
    input [255:0] b,
    output [511:0] p
);

    mult_8_pipelined_Nclk #(.N(32)) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
