///////////////////////////////////////////
//  Functionality: 8-bit Pipelined Multiplier
//  Author:        Xifan Tang
////////////////////////////////////////

module mult_8_pipelined (
    clk,
    a,
    b,
    p
);

    input clk;
    input [7:0] a;
    input [7:0] b;
    output [15:0] p;

    reg [7:0] a_reg;
    reg [7:0] b_reg;
    reg [15:0] p;

    // Stage 1: Register Inputs
    always @(posedge clk) begin
        a_reg <= a;
        b_reg <= b;
    end

    // Stage 2: Register Output Product
    always @(posedge clk) begin
        p <= a_reg * b_reg;
    end

endmodule
