//-------------------------------------------------------
//  Functionality: A 32-bit combinatorial square, where
//                 the same input drives both operands
//                 of the multiply
//  Author:        Amin Mohaghegh
//-------------------------------------------------------

module square_32(A, Y);
parameter DATA_WIDTH = 32;  /* declare a parameter. default required */
input [DATA_WIDTH - 1 : 0] A;
output [DATA_WIDTH + DATA_WIDTH - 1 : 0] Y;

assign Y = A * A;

endmodule
