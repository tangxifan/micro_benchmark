/////////////////////////////////////////
//  Functionality: four 16 bit down counters 
//			 operating upon 4 different clocks 
////////////////////////////////////////

module down_counter16 (clk, reset, count);
	input clk, reset;
	output [15:0] count;
	reg [15:0] count;                                   

	always @ (posedge clk or negedge reset) begin
		if (reset == 1'b0)
		  count <= 16'hffff;
		else 
		  count <= count - 1;
	end

endmodule  

module down_counter16_4 (clock0, clock1, clock2, clock3, reset, cnt0_16, cnt1_16, cnt2_16, cnt3_16);
	input clock0, clock1, clock2, clock3;
	input reset;
	output [15:0] cnt0_16;
	output [15:0] cnt1_16;
	output [15:0] cnt2_16;
	output [15:0] cnt3_16;

	down_counter16 u_cnt0(.clk(clock0), .reset(reset), .count(cnt0_16));
	down_counter16 u_cnt1(.clk(clock1), .reset(reset), .count(cnt1_16));
	down_counter16 u_cnt2(.clk(clock2), .reset(reset), .count(cnt2_16));
	down_counter16 u_cnt3(.clk(clock3), .reset(reset), .count(cnt3_16));

endmodule 