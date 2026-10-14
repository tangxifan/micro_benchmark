`timescale 1ns / 1ps

module clock_divider (clk_in, clk_out);
  input clk_in;
  output reg clk_out;
    
    parameter CLK_DIVIDER_SIZE=8;
    
    reg [CLK_DIVIDER_SIZE - 1:0] clkdiv_counter;
    
    initial begin
      clkdiv_counter <= 0;
      clk_out <= 0;
    end
    
    // Divide pl_clk (50MHz) to 1MHz
    always @(posedge clk_in) begin
        if (clkdiv_counter == 1 << CLK_DIVIDER_SIZE - 1) begin
            clk_out <= ~clk_out;
        end
        clkdiv_counter <= clkdiv_counter +1;
    end
    
endmodule
