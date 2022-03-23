/////////////////////////////////////////
//  Functionality: 16 bit up counter 
////////////////////////////////////////

module counter16_pos_rst(clock0, reset, count);

	input clock0, reset;
	output [15:0] count;
	reg [15:0] count;                                   

	always @ (posedge clock0 or posedge reset) begin
		if (reset == 1'b1) begin
			count <= 0;
		end 
		else begin
			count <= count + 1;
		end
	end

`ifdef COCOTB_SIM
initial begin
  $dumpfile ("counter16_pos_rst.vcd");
  $dumpvars (0,counter16_pos_rst);
  #1;
end
`endif  

endmodule
