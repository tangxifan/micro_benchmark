///////////////////////////////////////////
//  Functionality: 24-Clock 8-bit Countdown Timer with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module timer8_24clk_async_reset (
    input clk0,  input clk1,  input clk2,  input clk3,  input clk4,  input clk5,  input clk6,  input clk7,
    input clk8,  input clk9,  input clk10, input clk11, input clk12, input clk13, input clk14, input clk15,
    input clk16, input clk17, input clk18, input clk19, input clk20, input clk21, input clk22, input clk23,
    input reset,
    input en0,  input en1,  input en2,  input en3,  input en4,  input en5,  input en6,  input en7,
    input en8,  input en9,  input en10, input en11, input en12, input en13, input en14, input en15,
    input en16, input en17, input en18, input en19, input en20, input en21, input en22, input en23,
    input [7:0] period0,  input [7:0] period1,  input [7:0] period2,  input [7:0] period3,
    input [7:0] period4,  input [7:0] period5,  input [7:0] period6,  input [7:0] period7,
    input [7:0] period8,  input [7:0] period9,  input [7:0] period10, input [7:0] period11,
    input [7:0] period12, input [7:0] period13, input [7:0] period14, input [7:0] period15,
    input [7:0] period16, input [7:0] period17, input [7:0] period18, input [7:0] period19,
    input [7:0] period20, input [7:0] period21, input [7:0] period22, input [7:0] period23,
    output [7:0] count0,  output [7:0] count1,  output [7:0] count2,  output [7:0] count3,
    output [7:0] count4,  output [7:0] count5,  output [7:0] count6,  output [7:0] count7,
    output [7:0] count8,  output [7:0] count9,  output [7:0] count10, output [7:0] count11,
    output [7:0] count12, output [7:0] count13, output [7:0] count14, output [7:0] count15,
    output [7:0] count16, output [7:0] count17, output [7:0] count18, output [7:0] count19,
    output [7:0] count20, output [7:0] count21, output [7:0] count22, output [7:0] count23,
    output timer_done0,  output timer_done1,  output timer_done2,  output timer_done3,
    output timer_done4,  output timer_done5,  output timer_done6,  output timer_done7,
    output timer_done8,  output timer_done9,  output timer_done10, output timer_done11,
    output timer_done12, output timer_done13, output timer_done14, output timer_done15,
    output timer_done16, output timer_done17, output timer_done18, output timer_done19,
    output timer_done20, output timer_done21, output timer_done22, output timer_done23
);

    // Instantiate Timers 0 to 23
    timer8_async_reset u_timer0  (.clk(clk0),  .reset(reset), .en(en0),  .period(period0),  .count(count0),  .timer_done(timer_done0));
    timer8_async_reset u_timer1  (.clk(clk1),  .reset(reset), .en(en1),  .period(period1),  .count(count1),  .timer_done(timer_done1));
    timer8_async_reset u_timer2  (.clk(clk2),  .reset(reset), .en(en2),  .period(period2),  .count(count2),  .timer_done(timer_done2));
    timer8_async_reset u_timer3  (.clk(clk3),  .reset(reset), .en(en3),  .period(period3),  .count(count3),  .timer_done(timer_done3));
    timer8_async_reset u_timer4  (.clk(clk4),  .reset(reset), .en(en4),  .period(period4),  .count(count4),  .timer_done(timer_done4));
    timer8_async_reset u_timer5  (.clk(clk5),  .reset(reset), .en(en5),  .period(period5),  .count(count5),  .timer_done(timer_done5));
    timer8_async_reset u_timer6  (.clk(clk6),  .reset(reset), .en(en6),  .period(period6),  .count(count6),  .timer_done(timer_done6));
    timer8_async_reset u_timer7  (.clk(clk7),  .reset(reset), .en(en7),  .period(period7),  .count(count7),  .timer_done(timer_done7));
    timer8_async_reset u_timer8  (.clk(clk8),  .reset(reset), .en(en8),  .period(period8),  .count(count8),  .timer_done(timer_done8));
    timer8_async_reset u_timer9  (.clk(clk9),  .reset(reset), .en(en9),  .period(period9),  .count(count9),  .timer_done(timer_done9));
    timer8_async_reset u_timer10 (.clk(clk10), .reset(reset), .en(en10), .period(period10), .count(count10), .timer_done(timer_done10));
    timer8_async_reset u_timer11 (.clk(clk11), .reset(reset), .en(en11), .period(period11), .count(count11), .timer_done(timer_done11));
    timer8_async_reset u_timer12 (.clk(clk12), .reset(reset), .en(en12), .period(period12), .count(count12), .timer_done(timer_done12));
    timer8_async_reset u_timer13 (.clk(clk13), .reset(reset), .en(en13), .period(period13), .count(count13), .timer_done(timer_done13));
    timer8_async_reset u_timer14 (.clk(clk14), .reset(reset), .en(en14), .period(period14), .count(count14), .timer_done(timer_done14));
    timer8_async_reset u_timer15 (.clk(clk15), .reset(reset), .en(en15), .period(period15), .count(count15), .timer_done(timer_done15));
    timer8_async_reset u_timer16 (.clk(clk16), .reset(reset), .en(en16), .period(period16), .count(count16), .timer_done(timer_done16));
    timer8_async_reset u_timer17 (.clk(clk17), .reset(reset), .en(en17), .period(period17), .count(count17), .timer_done(timer_done17));
    timer8_async_reset u_timer18 (.clk(clk18), .reset(reset), .en(en18), .period(period18), .count(count18), .timer_done(timer_done18));
    timer8_async_reset u_timer19 (.clk(clk19), .reset(reset), .en(en19), .period(period19), .count(count19), .timer_done(timer_done19));
    timer8_async_reset u_timer20 (.clk(clk20), .reset(reset), .en(en20), .period(period20), .count(count20), .timer_done(timer_done20));
    timer8_async_reset u_timer21 (.clk(clk21), .reset(reset), .en(en21), .period(period21), .count(count21), .timer_done(timer_done21));
    timer8_async_reset u_timer22 (.clk(clk22), .reset(reset), .en(en22), .period(period22), .count(count22), .timer_done(timer_done22));
    timer8_async_reset u_timer23 (.clk(clk23), .reset(reset), .en(en23), .period(period23), .count(count23), .timer_done(timer_done23));

endmodule
