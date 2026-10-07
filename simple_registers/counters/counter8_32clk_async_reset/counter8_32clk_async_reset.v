///////////////////////////////////////////
// Functionality: 32-Clock 8-bit Counter with Asynchronous Reset
///////////////////////////////////////////

module counter8_32clk_async_reset (
    input [31:0] clk,
    input reset,
    output [255:0] result
);

    counter8_Nclk_async_reset #(.N(32)) core (
        .clk(clk),
        .reset(reset),
        .result(result)
    );

endmodule
