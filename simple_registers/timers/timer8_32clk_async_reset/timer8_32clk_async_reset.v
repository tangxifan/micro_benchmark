///////////////////////////////////////////
// Functionality: 32-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_32clk_async_reset (
    input [31:0] clk,
    input reset,
    input [31:0] en,
    input [255:0] period,
    output [255:0] count,
    output [31:0] timer_done
);

    timer8_Nclk_async_reset #(.N(32)) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
