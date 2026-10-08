///////////////////////////////////////////
//  Functionality: 4-Clock Counter with asynchronous reset
//  Author:        Xifan Tang
////////////////////////////////////////
module counter8_4clk_async_reset (
	clk0,
	clk1,
	clk2,
	clk3,
	reset,
	result0,
	result1,
	result2,
	result3
);

	input clk0;
	input clk1;
	input clk2;
	input clk3;
	input reset;
	output [7:0] result0;
	output [7:0] result1;
	output [7:0] result2;
	output [7:0] result3;

	reg [7:0] result0;
	reg [7:0] result1;
	reg [7:0] result2;
	reg [7:0] result3;

	// Counter 0
	always @(posedge clk0 or posedge reset) begin
		if (reset) 
			result0 <= 8'h00;		
		else 
			result0 <= result0 + 1'b1;
	end

	// Counter 1
	always @(posedge clk1 or posedge reset) begin
		if (reset) 
			result1 <= 8'h00;		
		else 
			result1 <= result1 + 1'b1;
	end

	// Counter 2
	always @(posedge clk2 or posedge reset) begin
		if (reset) 
			result2 <= 8'h00;		
		else 
			result2 <= result2 + 1'b1;
	end

	// Counter 3
	always @(posedge clk3 or posedge reset) begin
		if (reset) 
			result3 <= 8'h00;		
		else 
			result3 <= result3 + 1'b1;
	end
    // Add this block at the bottom of your top-level module:
    `ifdef COCOTB_SIM
    initial begin
        $dumpfile("extension_waves.vcd"); // Name of the VCD file
        $dumpvars(0, counter8_4clk_async_reset);          // 0 means dump all signals in this module and below
        #1;
    end
    `endif

endmodule
