///////////////////////////////////////////
// Functionality: 8-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_8clk (
    input [7:0] clk,
    input [63:0] a,
    input [63:0] b,
    output [127:0] p
);

    mult_8_pipelined_Nclk #(.N(8)) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
