///////////////////////////////////////////
//  Functionality: 8-Clock Dual-Port RAM (8x16) Hierarchical Wrapper with Flattened Ports
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_8clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire        clk_a0,  input  wire        clk_a1,  input  wire        clk_a2,  input  wire        clk_a3,
    input  wire        clk_a4,  input  wire        clk_a5,  input  wire        clk_a6,  input  wire        clk_a7,
    input  wire        we_a0,   input  wire        we_a1,   input  wire        we_a2,   input  wire        we_a3,
    input  wire        we_a4,   input  wire        we_a5,   input  wire        we_a6,   input  wire        we_a7,
    input  wire [7:0]  addr_a0, input  wire [7:0]  addr_a1, input  wire [7:0]  addr_a2, input  wire [7:0]  addr_a3,
    input  wire [7:0]  addr_a4, input  wire [7:0]  addr_a5, input  wire [7:0]  addr_a6, input  wire [7:0]  addr_a7,
    input  wire [15:0] din_a0,  input  wire [15:0] din_a1,  input  wire [15:0] din_a2,  input  wire [15:0] din_a3,
    input  wire [15:0] din_a4,  input  wire [15:0] din_a5,  input  wire [15:0] din_a6,  input  wire [15:0] din_a7,
    
    input  wire        clk_b0,  input  wire        clk_b1,  input  wire        clk_b2,  input  wire        clk_b3,
    input  wire        clk_b4,  input  wire        clk_b5,  input  wire        clk_b6,  input  wire        clk_b7,
    input  wire [7:0]  addr_b0, input  wire [7:0]  addr_b1, input  wire [7:0]  addr_b2, input  wire [7:0]  addr_b3,
    input  wire [7:0]  addr_b4, input  wire [7:0]  addr_b5, input  wire [7:0]  addr_b6, input  wire [7:0]  addr_b7,
    output wire [15:0] dout_b0, output wire [15:0] dout_b1, output wire [15:0] dout_b2, output wire [15:0] dout_b3,
    output wire [15:0] dout_b4, output wire [15:0] dout_b5, output wire [15:0] dout_b6, output wire [15:0] dout_b7
);

    // Instantiate Instances 0 to 7[cite: 3]
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram0 (.clk_a(clk_a0), .we_a(we_a0), .addr_a(addr_a0), .din_a(din_a0), .clk_b(clk_b0), .addr_b(addr_b0), .dout_b(dout_b0));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram1 (.clk_a(clk_a1), .we_a(we_a1), .addr_a(addr_a1), .din_a(din_a1), .clk_b(clk_b1), .addr_b(addr_b1), .dout_b(dout_b1));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram2 (.clk_a(clk_a2), .we_a(we_a2), .addr_a(addr_a2), .din_a(din_a2), .clk_b(clk_b2), .addr_b(addr_b2), .dout_b(dout_b2));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram3 (.clk_a(clk_a3), .we_a(we_a3), .addr_a(addr_a3), .din_a(din_a3), .clk_b(clk_b3), .addr_b(addr_b3), .dout_b(dout_b3));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram4 (.clk_a(clk_a4), .we_a(we_a4), .addr_a(addr_a4), .din_a(din_a4), .clk_b(clk_b4), .addr_b(addr_b4), .dout_b(dout_b4));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram5 (.clk_a(clk_a5), .we_a(we_a5), .addr_a(addr_a5), .din_a(din_a5), .clk_b(clk_b5), .addr_b(addr_b5), .dout_b(dout_b5));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram6 (.clk_a(clk_a6), .we_a(we_a6), .addr_a(addr_a6), .din_a(din_a6), .clk_b(clk_b6), .addr_b(addr_b6), .dout_b(dout_b6));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram7 (.clk_a(clk_a7), .we_a(we_a7), .addr_a(addr_a7), .din_a(din_a7), .clk_b(clk_b7), .addr_b(addr_b7), .dout_b(dout_b7));

endmodule
