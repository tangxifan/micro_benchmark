//-------------------------------------------------------
//  Functionality: A 2-bit combinatorial multiply
//  Author:        Xifan Tang
//-------------------------------------------------------

module mult_2x2(A, B, Y);
parameter DATA_WIDTH = 2;  /* declare a parameter. default required */
input [DATA_WIDTH - 1 : 0] A, B;
output [DATA_WIDTH + DATA_WIDTH - 1 : 0] Y;

assign Y = A * B;

endmodule









