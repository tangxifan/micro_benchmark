///////////////////////////////////////////
//  Functionality: Counter with asynchronous reset
//  Author:        Xifan Tang
////////////////////////////////////////

module counter8_async_reset (
	clk,
	reset,
	result
);

	input clk;
	input reset;
	output [7:0] result;

	reg [7:0] result;

	always @(posedge clk or posedge reset)
	begin
		if (reset) 
			result = 0;		
		else 
			result = result + 1;
	end
endmodule		