//-------------------------------------------------------
//  Functionality: A 2-bit combinatorial multiply
//  Author:        Xifan Tang
//-------------------------------------------------------

module mult_2x2(a, b, out);
parameter DATA_WIDTH = 2;  /* declare a parameter. default required */
input [DATA_WIDTH - 1 : 0] a, b;
output [DATA_WIDTH - 1 : 0] out;

assign out = a * b;

endmodule









