///////////////////////////////////////////
//  Functionality: Parameterized N-Clock 8-bit Countdown Timer
//  Author:        Xifan Tang
////////////////////////////////////////

module timer8_Nclk_async_reset #(
    parameter N = 4
)(
    input  wire [N-1:0]     clk,
    input  wire             reset,
    input  wire [N-1:0]     en,
    input  wire [N*8-1:0]   period,
    output reg  [N*8-1:0]   count,
    output reg  [N-1:0]     timer_done
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_timer
            always @(posedge clk[i] or posedge reset) begin
                if (reset) begin
                    count[i*8 +: 8]      <= 8'h00;
                    timer_done[i]        <= 1'b0;
                end else if (en[i]) begin
                    if (count[i*8 +: 8] == 8'h00) begin
                        count[i*8 +: 8]  <= period[i*8 +: 8];
                        timer_done[i]    <= 1'b1;
                    end else begin
                        count[i*8 +: 8]  <= count[i*8 +: 8] - 1'b1;
                        timer_done[i]    <= 1'b0;
                    end
                end else begin
                    timer_done[i]        <= 1'b0;
                end
            end
        end
    endgenerate

endmodule
