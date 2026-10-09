///////////////////////////////////////////
//  Functionality: 4-Clock Counter with asynchronous reset (Hierarchical)
//  Author:        Xifan Tang
////////////////////////////////////////
module counter8_4clk_async_reset (
    input clk0,
    input clk1,
    input clk2,
    input clk3,
    input reset,
    output [7:0] result0,
    output [7:0] result1,
    output [7:0] result2,
    output [7:0] result3
);

    // Instantiate Counter 0
    counter8_async_reset u_counter0 (
        .clk(clk0),
        .reset(reset),
        .result(result0)
    );

    // Instantiate Counter 1
    counter8_async_reset u_counter1 (
        .clk(clk1),
        .reset(reset),
        .result(result1)
    );

    // Instantiate Counter 2
    counter8_async_reset u_counter2 (
        .clk(clk2),
        .reset(reset),
        .result(result2)
    );

    // Instantiate Counter 3
    counter8_async_reset u_counter3 (
        .clk(clk3),
        .reset(reset),
        .result(result3)
    );

endmodule
