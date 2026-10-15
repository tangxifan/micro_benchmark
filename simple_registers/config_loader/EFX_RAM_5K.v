`timescale 1ns / 1ps

module EFX_RAM_5K (
    input WDATA,
    input [13:0] WADDR,
    input WE,
    input WCLK,
    input WCLKE,
    output reg RDATA,
    input [13:0] RADDR,
    input RE,
    input RCLK
);
    parameter READ_WIDTH = 1;
    parameter WRITE_WIDTH = 0;

    parameter [255:0] INIT_0  = 256'h0;
    parameter [255:0] INIT_1  = 256'h0;
    parameter [255:0] INIT_2  = 256'h0;
    parameter [255:0] INIT_3  = 256'h0;
    parameter [255:0] INIT_4  = 256'h0;
    parameter [255:0] INIT_5  = 256'h0;
    parameter [255:0] INIT_6  = 256'h0;
    parameter [255:0] INIT_7  = 256'h0;
    parameter [255:0] INIT_8  = 256'h0;
    parameter [255:0] INIT_9  = 256'h0;
    parameter [255:0] INIT_A  = 256'h0;
    parameter [255:0] INIT_B  = 256'h0;
    parameter [255:0] INIT_C  = 256'h0;
    parameter [255:0] INIT_D  = 256'h0;
    parameter [255:0] INIT_E  = 256'h0;
    parameter [255:0] INIT_F  = 256'h0;
    parameter [255:0] INIT_10 = 256'h0;
    parameter [255:0] INIT_11 = 256'h0;
    parameter [255:0] INIT_12 = 256'h0;
    parameter [255:0] INIT_13 = 256'h0;
    parameter [255:0] INIT_14 = 256'h0;
    parameter [255:0] INIT_15 = 256'h0;
    parameter [255:0] INIT_16 = 256'h0;
    parameter [255:0] INIT_17 = 256'h0;

    // Behavioral memory array for simulation (16,383 bits total capacity)
    reg [0:0] mem [0:16383];

    integer i;

    initial begin
        // Clear memory by default
        for (i = 0; i < 16384; i = i + 1) begin
            mem[i] = 1'b0;
        end

        // Load 256-bit INIT blocks into corresponding memory addresses
        for (i = 0; i < 256; i = i + 1) begin
            mem[0  + i] = INIT_0[i];
            mem[256 + i] = INIT_1[i];
            mem[512 + i] = INIT_2[i];
            mem[768 + i] = INIT_3[i];
            mem[1024 + i] = INIT_4[i];
            mem[1280 + i] = INIT_5[i];
            mem[1536 + i] = INIT_6[i];
            mem[1792 + i] = INIT_7[i];
            mem[2048 + i] = INIT_8[i];
            mem[2304 + i] = INIT_9[i];
            mem[2560 + i] = INIT_A[i];
            mem[2816 + i] = INIT_B[i];
            mem[3072 + i] = INIT_C[i];
            mem[3328 + i] = INIT_D[i];
            mem[3584 + i] = INIT_E[i];
            mem[3840 + i] = INIT_F[i];
            mem[4096 + i] = INIT_10[i];
            mem[4352 + i] = INIT_11[i];
            mem[4608 + i] = INIT_12[i];
            mem[4864 + i] = INIT_13[i];
            mem[5120 + i] = INIT_14[i];
            mem[5376 + i] = INIT_15[i];
            mem[5632 + i] = INIT_16[i];
            mem[5888 + i] = INIT_17[i];
        end
    end

    always @(posedge RCLK) begin
        if (RE) begin
            RDATA <= mem[RADDR];
        end
    end
endmodule