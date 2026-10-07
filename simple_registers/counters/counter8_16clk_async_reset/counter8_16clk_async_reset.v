///////////////////////////////////////////
// Functionality: 16-Clock 8-bit Counter with Asynchronous Reset
///////////////////////////////////////////

module counter8_16clk_async_reset (
    input [15:0] clk,
    input reset,
    output [127:0] result
);

    counter8_Nclk_async_reset #(.N(16)) core (
        .clk(clk),
        .reset(reset),
        .result(result)
    );

endmodule
