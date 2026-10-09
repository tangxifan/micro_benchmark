///////////////////////////////////////////
//  Functionality: 8-Clock Counter with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module counter8_8clk_async_reset (
    input clk0,
    input clk1,
    input clk2,
    input clk3,
    input clk4,
    input clk5,
    input clk6,
    input clk7,
    input reset,
    output [7:0] result0,
    output [7:0] result1,
    output [7:0] result2,
    output [7:0] result3,
    output [7:0] result4,
    output [7:0] result5,
    output [7:0] result6,
    output [7:0] result7
);

    counter8_async_reset u_counter0 (.clk(clk0), .reset(reset), .result(result0));
    counter8_async_reset u_counter1 (.clk(clk1), .reset(reset), .result(result1));
    counter8_async_reset u_counter2 (.clk(clk2), .reset(reset), .result(result2));
    counter8_async_reset u_counter3 (.clk(clk3), .reset(reset), .result(result3));
    counter8_async_reset u_counter4 (.clk(clk4), .reset(reset), .result(result4));
    counter8_async_reset u_counter5 (.clk(clk5), .reset(reset), .result(result5));
    counter8_async_reset u_counter6 (.clk(clk6), .reset(reset), .result(result6));
    counter8_async_reset u_counter7 (.clk(clk7), .reset(reset), .result(result7));

endmodule
