///////////////////////////////////////////
//  Functionality: Parameterized N-Clock 8-bit Pipelined Multiplier
//  Author:        Xifan Tang
////////////////////////////////////////

module mult_8_pipelined_Nclk #(
    parameter N = 4
)(
    input  wire [N-1:0]     clk,
    input  wire [N*8-1:0]   a,
    input  wire [N*8-1:0]   b,
    output reg  [N*16-1:0]  p
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_mult
            // Stage 1 Pipeline Registers
            reg [7:0] a_reg;
            reg [7:0] b_reg;

            always @(posedge clk[i]) begin
                a_reg <= a[i*8 +: 8];
                b_reg <= b[i*8 +: 8];
            end

            // Stage 2 Pipeline Output Register
            always @(posedge clk[i]) begin
                p[i*16 +: 16] <= a_reg * b_reg;
            end
        end
    endgenerate

endmodule
