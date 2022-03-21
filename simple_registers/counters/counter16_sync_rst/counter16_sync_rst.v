/////////////////////////////////////////
//  Functionality: 16 bit up counter 
////////////////////////////////////////

module counter16_sync_rst(clock0, reset, count);

	input clock0, reset;
	output [15:0] count;
	reg [15:0] count;                                   

	always @ (posedge clock0) begin
		if (reset == 1'b0) begin
			count <= 0;
		end 
		else begin
			count <= count + 1;
		end
	end

endmodule
