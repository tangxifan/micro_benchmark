//-------------------------------------------------------
//  Functionality: A 4-bit combinatorial multiply
//  Author:        Xifan Tang
//-------------------------------------------------------

module mult_4x4(A, B, Y);
parameter DATA_WIDTH = 4;  /* declare a parameter. default required */
input [DATA_WIDTH - 1 : 0] A, B;
output [DATA_WIDTH + DATA_WIDTH - 1 : 0] Y;

assign Y = A * B;

endmodule









