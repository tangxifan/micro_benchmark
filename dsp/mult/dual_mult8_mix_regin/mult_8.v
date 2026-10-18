//-----------------------------------------------------
// Design Name : mult_8
// File Name   : mult_8.v
// Function    : A 8-bit multiplier
// Coder       : Xifan Tang
//-----------------------------------------------------

module mult_8 (
  input [0:7] A,
  input [0:7] B,
  output [0:15] Y
);

  assign Y = A * B;

endmodule

