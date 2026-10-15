module reset_generator(
	input clk,
	output reg pulse
	);

	parameter INITIAL_VALUE=0; 
	parameter ACTIVE_CYCLES=0; 

	reg [ACTIVE_CYCLES<=2 ? 2 : $clog2(ACTIVE_CYCLES) - 1 : 0] active_cycle_counter;

	initial begin
		active_cycle_counter <= 0;
		pulse <= INITIAL_VALUE;
	end

	// Wait a number of clock cycles, hold the initial value
	always @(posedge clk) begin
		if (active_cycle_counter == ACTIVE_CYCLES) begin
			pulse <= ~pulse;
		end else begin 
			active_cycle_counter <= active_cycle_counter + 1;
		end
	end

endmodule