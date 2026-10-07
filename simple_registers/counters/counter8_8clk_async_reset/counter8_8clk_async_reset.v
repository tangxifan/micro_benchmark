///////////////////////////////////////////
// Functionality: 8-Clock 8-bit Counter with Asynchronous Reset
///////////////////////////////////////////

module counter8_8clk_async_reset (
    input [7:0] clk,
    input reset,
    output [63:0] result
);

    counter8_Nclk_async_reset #(.N(8)) core (
        .clk(clk),
        .reset(reset),
        .result(result)
    );

endmodule
