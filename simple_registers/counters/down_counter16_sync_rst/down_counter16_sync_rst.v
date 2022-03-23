/////////////////////////////////////////
//  Functionality: 16 bit down counter 
////////////////////////////////////////

module down_counter16_sync_rst(clock0, reset, count);

	input clock0, reset;
	output [15:0] count;
	reg [15:0] count;                                   

	always @ (posedge clock0) begin
		if (reset == 1'b0) begin
			count <= 16'hffff;
		end 
		else begin
			count <= count - 1;
		end
	end

endmodule
