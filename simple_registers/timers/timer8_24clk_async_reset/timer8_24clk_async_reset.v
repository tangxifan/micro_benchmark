///////////////////////////////////////////
// Functionality: 24-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_24clk_async_reset (
    input [23:0] clk,
    input reset,
    input [23:0] en,
    input [191:0] period,
    output [191:0] count,
    output [23:0] timer_done
);

    timer8_Nclk_async_reset #(.N(24)) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
