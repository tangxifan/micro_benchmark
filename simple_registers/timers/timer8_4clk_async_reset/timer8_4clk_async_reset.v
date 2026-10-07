///////////////////////////////////////////
// Functionality: 4-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_4clk_async_reset (
    input [3:0] clk,
    input reset,
    input [3:0] en,
    input [31:0] period,
    output [31:0] count,
    output [3:0] timer_done
);

    timer8_Nclk_async_reset #(.N(4)) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
