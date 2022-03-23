/////////////////////////////////////////
//  Functionality: 16 bit down counter 
////////////////////////////////////////

module down_counter16(clock0, reset, count);

	input clock0, reset;
	output [15:0] count;
	reg [15:0] count;                                   

	always @ (posedge clock0 or negedge reset) begin
		if (reset == 1'b0) begin
			count <= 16'hffff;
		end 
		else begin
			count <= count - 1;
		end
	end

`ifdef COCOTB_SIM
initial begin
  $dumpfile ("down_count16.vcd");
  $dumpvars (0,down_counter16);
  #1;
end
`endif  

endmodule
