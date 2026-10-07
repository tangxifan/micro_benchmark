///////////////////////////////////////////
// Functionality: 24-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_24clk (
    input [23:0] clk,
    input [191:0] a,
    input [191:0] b,
    output [383:0] p
);

    mult_8_pipelined_Nclk #(.N(24)) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
