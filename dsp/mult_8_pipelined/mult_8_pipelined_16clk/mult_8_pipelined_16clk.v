///////////////////////////////////////////
// Functionality: 16-Clock 8-bit Pipelined Multiplier
///////////////////////////////////////////

module mult_8_pipelined_16clk (
    input [15:0] clk,
    input [127:0] a,
    input [127:0] b,
    output [255:0] p
);

    mult_8_pipelined_Nclk #(.N(16)) core (
        .clk(clk),
        .a(a),
        .b(b),
        .p(p)
    );

endmodule
