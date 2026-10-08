///////////////////////////////////////////
//  Functionality: 32-Clock Counter with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module counter8_32clk_async_reset (
    input clk0,  input clk1,  input clk2,  input clk3,
    input clk4,  input clk5,  input clk6,  input clk7,
    input clk8,  input clk9,  input clk10, input clk11,
    input clk12, input clk13, input clk14, input clk15,
    input clk16, input clk17, input clk18, input clk19,
    input clk20, input clk21, input clk22, input clk23,
    input clk24, input clk25, input clk26, input clk27,
    input clk28, input clk29, input clk30, input clk31,
    input reset,
    output [7:0] result0,  output [7:0] result1,  output [7:0] result2,  output [7:0] result3,
    output [7:0] result4,  output [7:0] result5,  output [7:0] result6,  output [7:0] result7,
    output [7:0] result8,  output [7:0] result9,  output [7:0] result10, output [7:0] result11,
    output [7:0] result12, output [7:0] result13, output [7:0] result14, output [7:0] result15,
    output [7:0] result16, output [7:0] result17, output [7:0] result18, output [7:0] result19,
    output [7:0] result20, output [7:0] result21, output [7:0] result22, output [7:0] result23,
    output [7:0] result24, output [7:0] result25, output [7:0] result26, output [7:0] result27,
    output [7:0] result28, output [7:0] result29, output [7:0] result30, output [7:0] result31
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
    counter8_async_reset u_counter16 (.clk(clk16), .reset(reset), .result(result16));
    counter8_async_reset u_counter17 (.clk(clk17), .reset(reset), .result(result17));
    counter8_async_reset u_counter18 (.clk(clk18), .reset(reset), .result(result18));
    counter8_async_reset u_counter19 (.clk(clk19), .reset(reset), .result(result19));
    counter8_async_reset u_counter20 (.clk(clk20), .reset(reset), .result(result20));
    counter8_async_reset u_counter21 (.clk(clk21), .reset(reset), .result(result21));
    counter8_async_reset u_counter22 (.clk(clk22), .reset(reset), .result(result22));
    counter8_async_reset u_counter23 (.clk(clk23), .reset(reset), .result(result23));
    counter8_async_reset u_counter24 (.clk(clk24), .reset(reset), .result(result24));
    counter8_async_reset u_counter25 (.clk(clk25), .reset(reset), .result(result25));
    counter8_async_reset u_counter26 (.clk(clk26), .reset(reset), .result(result26));
    counter8_async_reset u_counter27 (.clk(clk27), .reset(reset), .result(result27));
    counter8_async_reset u_counter28 (.clk(clk28), .reset(reset), .result(result28));
    counter8_async_reset u_counter29 (.clk(clk29), .reset(reset), .result(result29));
    counter8_async_reset u_counter30 (.clk(clk30), .reset(reset), .result(result30));
    counter8_async_reset u_counter31 (.clk(clk31), .reset(reset), .result(result31));

endmodule
