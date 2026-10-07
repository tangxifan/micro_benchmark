///////////////////////////////////////////
// Functionality: 24-Clock 8-bit Counter with Asynchronous Reset
///////////////////////////////////////////

module counter8_24clk_async_reset (
    input [23:0] clk,
    input reset,
    output [191:0] result
);

    counter8_Nclk_async_reset #(.N(24)) core (
        .clk(clk),
        .reset(reset),
        .result(result)
    );

endmodule
