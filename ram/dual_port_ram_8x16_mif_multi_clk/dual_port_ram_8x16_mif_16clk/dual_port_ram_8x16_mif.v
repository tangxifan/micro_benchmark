///////////////////////////////////////////
//  Functionality: Single-Instance Dual-Port RAM (8x16) with Memory Preload
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire        clk_a,
    input  wire        we_a,
    input  wire [7:0]  addr_a,
    input  wire [15:0] din_a,
    
    input  wire        clk_b,
    input  wire [7:0]  addr_b,
    output reg  [15:0] dout_b
);

    reg [15:0] ram [0:255];

    initial begin
        if (RAM_INIT_FILE != "") begin
            $readmemh(RAM_INIT_FILE, ram);
        end
    end

    // Port A - Synchronous Write
    always @(posedge clk_a) begin
        if (we_a) begin
            ram[addr_a] <= din_a;
        end
    end

    // Port B - Synchronous Read
    always @(posedge clk_b) begin
        dout_b <= ram[addr_b];
    end

endmodule
