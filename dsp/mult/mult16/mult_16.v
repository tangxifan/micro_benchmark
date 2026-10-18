//-----------------------------------------------------
// Design Name : mult_16
// File Name   : mult_16.v
// Function    : A 16-bit multiplier
// Coder       : Xifan Tang
//-----------------------------------------------------

module mult_16 #(
    parameter MODE = 1
)(

  input [0:15] A,
  input [0:15] B,
  output [0:31] Y
);

  assign Y = A * B;

endmodule

