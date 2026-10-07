///////////////////////////////////////////
// Functionality: 8-Clock 8-bit Countdown Timer with Asynchronous Reset
///////////////////////////////////////////

module timer8_8clk_async_reset (
    input [7:0] clk,
    input reset,
    input [7:0] en,
    input [63:0] period,
    output [63:0] count,
    output [7:0] timer_done
);

    timer8_Nclk_async_reset #(.N(8)) core (
        .clk(clk),
        .reset(reset),
        .en(en),
        .period(period),
        .count(count),
        .timer_done(timer_done)
    );

endmodule
