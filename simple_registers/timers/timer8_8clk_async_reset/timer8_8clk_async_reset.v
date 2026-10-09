///////////////////////////////////////////
//  Functionality: 8-Clock 8-bit Countdown Timer with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module timer8_8clk_async_reset (
    input clk0,
    input clk1,
    input clk2,
    input clk3,
    input clk4,
    input clk5,
    input clk6,
    input clk7,
    input reset,
    input en0,
    input en1,
    input en2,
    input en3,
    input en4,
    input en5,
    input en6,
    input en7,
    input [7:0] period0,
    input [7:0] period1,
    input [7:0] period2,
    input [7:0] period3,
    input [7:0] period4,
    input [7:0] period5,
    input [7:0] period6,
    input [7:0] period7,
    output [7:0] count0,
    output [7:0] count1,
    output [7:0] count2,
    output [7:0] count3,
    output [7:0] count4,
    output [7:0] count5,
    output [7:0] count6,
    output [7:0] count7,
    output timer_done0,
    output timer_done1,
    output timer_done2,
    output timer_done3,
    output timer_done4,
    output timer_done5,
    output timer_done6,
    output timer_done7
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

    // Instantiate Timer 4
    timer8_async_reset u_timer4 (
        .clk(clk4),
        .reset(reset),
        .en(en4),
        .period(period4),
        .count(count4),
        .timer_done(timer_done4)
    );

    // Instantiate Timer 5
    timer8_async_reset u_timer5 (
        .clk(clk5),
        .reset(reset),
        .en(en5),
        .period(period5),
        .count(count5),
        .timer_done(timer_done5)
    );

    // Instantiate Timer 6
    timer8_async_reset u_timer6 (
        .clk(clk6),
        .reset(reset),
        .en(en6),
        .period(period6),
        .count(count6),
        .timer_done(timer_done6)
    );

    // Instantiate Timer 7
    timer8_async_reset u_timer7 (
        .clk(clk7),
        .reset(reset),
        .en(en7),
        .period(period7),
        .count(count7),
        .timer_done(timer_done7)
    );

endmodule
