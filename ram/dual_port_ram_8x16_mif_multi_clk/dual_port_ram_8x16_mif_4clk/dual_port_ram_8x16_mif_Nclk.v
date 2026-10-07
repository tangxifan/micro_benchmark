///////////////////////////////////////////
//  Functionality: Parameterized N-Instance Dual-Port RAM (8x16) with Memory Preload
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_Nclk #(
    parameter N = 4,
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire [N-1:0]      clk_a,
    input  wire [N-1:0]      we_a,
    input  wire [N*8-1:0]    addr_a,
    input  wire [N*16-1:0]   din_a,
    
    input  wire [N-1:0]      clk_b,
    input  wire [N*8-1:0]    addr_b,
    output reg  [N*16-1:0]   dout_b
);

    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin : g_dpram
            reg [15:0] ram [0:255];

            initial begin
                if (RAM_INIT_FILE != "") begin
                    $readmemh(RAM_INIT_FILE, ram);
                end
            end

            // Port A - Synchronous Write
            always @(posedge clk_a[i]) begin
                if (we_a[i]) begin
                    ram[addr_a[i*8 +: 8]] <= din_a[i*16 +: 16];
                end
            end

            // Port B - Synchronous Read
            always @(posedge clk_b[i]) begin
                dout_b[i*16 +: 16] <= ram[addr_b[i*8 +: 8]];
            end
        end
    endgenerate

endmodule
