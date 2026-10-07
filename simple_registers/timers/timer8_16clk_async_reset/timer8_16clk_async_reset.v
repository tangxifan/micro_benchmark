///////////////////////////////////////////
// Functionality: 16-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_16clk_async_reset (
    input [15:0] clk,
    input reset,
    input [15:0] en,
    input [127:0] period,
    output [127:0] count,
    output [15:0] timer_done
);

    timer8_Nclk_async_reset #(.N(16)) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
