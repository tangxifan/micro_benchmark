//-------------------------------------------------------
//  Functionality: A 32-bit combinatorial multiply
//  Author:        Amin Mohaghegh
//-------------------------------------------------------

module mult_32x32(A, B, Y);
parameter DATA_WIDTH = 32;  /* declare a parameter. default required */
input [DATA_WIDTH - 1 : 0] A, B;
output [DATA_WIDTH + DATA_WIDTH - 1 : 0] Y;

assign Y = A * B;

endmodule
