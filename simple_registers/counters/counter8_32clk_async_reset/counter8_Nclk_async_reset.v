///////////////////////////////////////////
//  Functionality: Parameterized N-Clock Counter with Asynchronous Reset
//  Author:        Xifan Tang
////////////////////////////////////////

module counter8_Nclk_async_reset #(
    parameter N = 8
)(
    input  wire [N-1:0]     clk,
    input  wire             reset,
    output reg  [N*8-1:0]   result
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_counter
            always @(posedge clk[i] or posedge reset) begin
                if (reset)
                    result[i*8 +: 8] <= 8'h00;
                else
                    result[i*8 +: 8] <= result[i*8 +: 8] + 1'b1;
            end
        end
    endgenerate

endmodule
