///////////////////////////////////////////
//  Functionality: 4-Clock Dual-Port RAM (8x16) Hierarchical Wrapper with Flattened Ports
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_4clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire        clk_a0,
    input  wire        clk_a1,
    input  wire        clk_a2,
    input  wire        clk_a3,
    input  wire        we_a0,
    input  wire        we_a1,
    input  wire        we_a2,
    input  wire        we_a3,
    input  wire [7:0]  addr_a0,
    input  wire [7:0]  addr_a1,
    input  wire [7:0]  addr_a2,
    input  wire [7:0]  addr_a3,
    input  wire [15:0] din_a0,
    input  wire [15:0] din_a1,
    input  wire [15:0] din_a2,
    input  wire [15:0] din_a3,
    
    input  wire        clk_b0,
    input  wire        clk_b1,
    input  wire        clk_b2,
    input  wire        clk_b3,
    input  wire [7:0]  addr_b0,
    input  wire [7:0]  addr_b1,
    input  wire [7:0]  addr_b2,
    input  wire [7:0]  addr_b3,
    output wire [15:0] dout_b0,
    output wire [15:0] dout_b1,
    output wire [15:0] dout_b2,
    output wire [15:0] dout_b3
);

    // Instantiate Instance 0
    dual_port_ram_8x16_mif #(
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) u_ram0 (
        .clk_a(clk_a0), .we_a(we_a0), .addr_a(addr_a0), .din_a(din_a0),
        .clk_b(clk_b0), .addr_b(addr_b0), .dout_b(dout_b0)
    );

    // Instantiate Instance 1
    dual_port_ram_8x16_mif #(
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) u_ram1 (
        .clk_a(clk_a1), .we_a(we_a1), .addr_a(addr_a1), .din_a(din_a1),
        .clk_b(clk_b1), .addr_b(addr_b1), .dout_b(dout_b1)
    );

    // Instantiate Instance 2
    dual_port_ram_8x16_mif #(
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) u_ram2 (
        .clk_a(clk_a2), .we_a(we_a2), .addr_a(addr_a2), .din_a(din_a2),
        .clk_b(clk_b2), .addr_b(addr_b2), .dout_b(dout_b2)
    );

    // Instantiate Instance 3
    dual_port_ram_8x16_mif #(
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) u_ram3 (
        .clk_a(clk_a3), .we_a(we_a3), .addr_a(addr_a3), .din_a(din_a3),
        .clk_b(clk_b3), .addr_b(addr_b3), .dout_b(dout_b3)
    );

endmodule
