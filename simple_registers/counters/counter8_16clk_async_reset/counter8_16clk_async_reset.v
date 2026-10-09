///////////////////////////////////////////
//  Functionality: 16-Clock Counter with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module counter8_16clk_async_reset (
    input clk0,  input clk1,  input clk2,  input clk3,
    input clk4,  input clk5,  input clk6,  input clk7,
    input clk8,  input clk9,  input clk10, input clk11,
    input clk12, input clk13, input clk14, input clk15,
    input reset,
    output [7:0] result0,  output [7:0] result1,  output [7:0] result2,  output [7:0] result3,
    output [7:0] result4,  output [7:0] result5,  output [7:0] result6,  output [7:0] result7,
    output [7:0] result8,  output [7:0] result9,  output [7:0] result10, output [7:0] result11,
    output [7:0] result12, output [7:0] result13, output [7:0] result14, output [7:0] result15
);

    counter8_async_reset u_counter0  (.clk(clk0),  .reset(reset), .result(result0));
    counter8_async_reset u_counter1  (.clk(clk1),  .reset(reset), .result(result1));
    counter8_async_reset u_counter2  (.clk(clk2),  .reset(reset), .result(result2));
    counter8_async_reset u_counter3  (.clk(clk3),  .reset(reset), .result(result3));
    counter8_async_reset u_counter4  (.clk(clk4),  .reset(reset), .result(result4));
    counter8_async_reset u_counter5  (.clk(clk5),  .reset(reset), .result(result5));
    counter8_async_reset u_counter6  (.clk(clk6),  .reset(reset), .result(result6));
    counter8_async_reset u_counter7  (.clk(clk7),  .reset(reset), .result(result7));
    counter8_async_reset u_counter8  (.clk(clk8),  .reset(reset), .result(result8));
    counter8_async_reset u_counter9  (.clk(clk9),  .reset(reset), .result(result9));
    counter8_async_reset u_counter10 (.clk(clk10), .reset(reset), .result(result10));
    counter8_async_reset u_counter11 (.clk(clk11), .reset(reset), .result(result11));
    counter8_async_reset u_counter12 (.clk(clk12), .reset(reset), .result(result12));
    counter8_async_reset u_counter13 (.clk(clk13), .reset(reset), .result(result13));
    counter8_async_reset u_counter14 (.clk(clk14), .reset(reset), .result(result14));
    counter8_async_reset u_counter15 (.clk(clk15), .reset(reset), .result(result15));

endmodule
