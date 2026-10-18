//-------------------------------------------------------
//  Module Name:   mult_8_regin
//  Functionality: 8-bit multiplier with input registers on ports A and B
//  Author:        Xifan Tang
//-------------------------------------------------------

module mult_8_regin #(
    parameter DATA_WIDTH = 8
)(
    input clk,
    input reset,
    input [0 : DATA_WIDTH - 1] A,
    input [0 : DATA_WIDTH - 1] B,
    output [0 : 2*DATA_WIDTH - 1] Y
);

    // Internal input registers for registered operands A and B
    reg [0 : DATA_WIDTH - 1] a_reg;
    reg [0 : DATA_WIDTH - 1] b_reg;

    // Synchronous input registration
    always @(posedge clk) begin
        if (reset) begin
            a_reg <= {DATA_WIDTH{1'b0}};
            b_reg <= {DATA_WIDTH{1'b0}};
        end else begin
            a_reg <= A;
            b_reg <= B;
        end
    end

    // Combinational multiplication of registered inputs
    assign Y = a_reg * b_reg;

endmodule
