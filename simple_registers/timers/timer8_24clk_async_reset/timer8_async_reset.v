///////////////////////////////////////////
//  Functionality: Single-Clock 8-bit Countdown Timer with asynchronous reset
//  Author:        Xifan Tang
////////////////////////////////////////

module timer8_async_reset (
    input  wire         clk,
    input  wire         reset,
    input  wire         en,
    input  wire   [7:0] period,
    output reg    [7:0] count,
    output reg          timer_done
);

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count      <= 8'h00;
            timer_done <= 1'b0;
        end else if (en) begin
            if (count == 8'h00) begin
                count  <= period;
                timer_done <= 1'b1;
            end else begin
                count  <= count - 1'b1;
                timer_done <= 1'b0;
            end
        end else begin
            timer_done <= 1'b0;
        end
    end

endmodule
