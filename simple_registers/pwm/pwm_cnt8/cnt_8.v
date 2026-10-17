//-----------------------------------------------------
// Design Name : 8-bit Counter with Match Outputs
// File Name   : cnt_8.v
// Coder       : Xifan TANG
//-----------------------------------------------------

module cnt_8 #(
  parameter [7:0] MATCH0_REF = 8'b11000000,
  parameter [7:0] MATCH1_REF = 8'b11110000
)(
  input clk,
  input rst,
  output match0,
  output match1
);

  reg [7:0] q_reg;

  always @(posedge clk) begin
    if (rst)
      q_reg <= 8'd0;
    else
      q_reg <= q_reg + 8'd1;
  end 

  assign match0 = (q_reg == MATCH0_REF) ? 1'b1 : 1'b0;
  assign match1 = (q_reg == MATCH1_REF) ? 1'b1 : 1'b0;
  
endmodule
