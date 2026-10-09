///////////////////////////////////////////
//  Functionality: 4-Clock 8-bit Countdown Timer with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module timer8_4clk_async_reset (
    input clk0,
    input clk1,
    input clk2,
    input clk3,
    input reset,
    input en0,
    input en1,
    input en2,
    input en3,
    input [7:0] period0,
    input [7:0] period1,
    input [7:0] period2,
    input [7:0] period3,
    output [7:0] count0,
    output [7:0] count1,
    output [7:0] count2,
    output [7:0] count3,
    output timer_done0,
    output timer_done1,
    output timer_done2,
    output timer_done3
);

    // Instantiate Timer 0
    timer8_async_reset u_timer0 (
        .clk(clk0),
        .reset(reset),
        .en(en0),
        .period(period0),
        .count(count0),
        .timer_done(timer_done0)
    );

    // Instantiate Timer 1
    timer8_async_reset u_timer1 (
        .clk(clk1),
        .reset(reset),
        .en(en1),
        .period(period1),
        .count(count1),
        .timer_done(timer_done1)
    );

    // Instantiate Timer 2
    timer8_async_reset u_timer2 (
        .clk(clk2),
        .reset(reset),
        .en(en2),
        .period(period2),
        .count(count2),
        .timer_done(timer_done2)
    );

    // Instantiate Timer 3
    timer8_async_reset u_timer3 (
        .clk(clk3),
        .reset(reset),
        .en(en3),
        .period(period3),
        .count(count3),
        .timer_done(timer_done3)
    );

endmodule
