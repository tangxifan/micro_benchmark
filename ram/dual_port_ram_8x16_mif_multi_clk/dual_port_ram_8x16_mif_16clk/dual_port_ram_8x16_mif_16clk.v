///////////////////////////////////////////
//  Functionality: 16-Clock Dual-Port RAM (8x16) Hierarchical Wrapper with Flattened Ports
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_16clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire        clk_a0,  input  wire        clk_a1,  input  wire        clk_a2,  input  wire        clk_a3,
    input  wire        clk_a4,  input  wire        clk_a5,  input  wire        clk_a6,  input  wire        clk_a7,
    input  wire        clk_a8,  input  wire        clk_a9,  input  wire        clk_a10, input  wire        clk_a11,
    input  wire        clk_a12, input  wire        clk_a13, input  wire        clk_a14, input  wire        clk_a15,
    input  wire        we_a0,   input  wire        we_a1,   input  wire        we_a2,   input  wire        we_a3,
    input  wire        we_a4,   input  wire        we_a5,   input  wire        we_a6,   input  wire        we_a7,
    input  wire        we_a8,   input  wire        we_a9,   input  wire        we_a10,  input  wire        we_a11,
    input  wire        we_a12,  input  wire        we_a13,  input  wire        we_a14,  input  wire        we_a15,
    input  wire [7:0]  addr_a0, input  wire [7:0]  addr_a1, input  wire [7:0]  addr_a2, input  wire [7:0]  addr_a3,
    input  wire [7:0]  addr_a4, input  wire [7:0]  addr_a5, input  wire [7:0]  addr_a6, input  wire [7:0]  addr_a7,
    input  wire [7:0]  addr_a8, input  wire [7:0]  addr_a9, input  wire [7:0]  addr_a10,input  wire [7:0]  addr_a11,
    input  wire [7:0]  addr_a12,input  wire [7:0]  addr_a13,input  wire [7:0]  addr_a14,input  wire [7:0]  addr_a15,
    input  wire [15:0] din_a0,  input  wire [15:0] din_a1,  input  wire [15:0] din_a2,  input  wire [15:0] din_a3,
    input  wire [15:0] din_a4,  input  wire [15:0] din_a5,  input  wire [15:0] din_a6,  input  wire [15:0] din_a7,
    input  wire [15:0] din_a8,  input  wire [15:0] din_a9,  input  wire [15:0] din_a10, input  wire [15:0] din_a11,
    input  wire [15:0] din_a12, input  wire [15:0] din_a13, input  wire [15:0] din_a14, input  wire [15:0] din_a15,
    
    input  wire        clk_b0,  input  wire        clk_b1,  input  wire        clk_b2,  input  wire        clk_b3,
    input  wire        clk_b4,  input  wire        clk_b5,  input  wire        clk_b6,  input  wire        clk_b7,
    input  wire        clk_b8,  input  wire        clk_b9,  input  wire        clk_b10, input  wire        clk_b11,
    input  wire        clk_b12, input  wire        clk_b13, input  wire        clk_b14, input  wire        clk_b15,
    input  wire [7:0]  addr_b0, input  wire [7:0]  addr_b1, input  wire [7:0]  addr_b2, input  wire [7:0]  addr_b3,
    input  wire [7:0]  addr_b4, input  wire [7:0]  addr_b5, input  wire [7:0]  addr_b6, input  wire [7:0]  addr_b7,
    input  wire [7:0]  addr_b8, input  wire [7:0]  addr_b9, input  wire [7:0]  addr_b10,input  wire [7:0]  addr_b11,
    input  wire [7:0]  addr_b12,input  wire [7:0]  addr_b13,input  wire [7:0]  addr_b14,input  wire [7:0]  addr_b15,
    output wire [15:0] dout_b0, output wire [15:0] dout_b1, output wire [15:0] dout_b2, output wire [15:0] dout_b3,
    output wire [15:0] dout_b4, output wire [15:0] dout_b5, output wire [15:0] dout_b6, output wire [15:0] dout_b7,
    output wire [15:0] dout_b8, output wire [15:0] dout_b9, output wire [15:0] dout_b10,output wire [15:0] dout_b11,
    output wire [15:0] dout_b12,output wire [15:0] dout_b13,output wire [15:0] dout_b14,output wire [15:0] dout_b15
);

    // Instantiate Instances 0 to 15
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram0  (.clk_a(clk_a0),  .we_a(we_a0),  .addr_a(addr_a0),  .din_a(din_a0),  .clk_b(clk_b0),  .addr_b(addr_b0),  .dout_b(dout_b0));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram1  (.clk_a(clk_a1),  .we_a(we_a1),  .addr_a(addr_a1),  .din_a(din_a1),  .clk_b(clk_b1),  .addr_b(addr_b1),  .dout_b(dout_b1));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram2  (.clk_a(clk_a2),  .we_a(we_a2),  .addr_a(addr_a2),  .din_a(din_a2),  .clk_b(clk_b2),  .addr_b(addr_b2),  .dout_b(dout_b2));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram3  (.clk_a(clk_a3),  .we_a(we_a3),  .addr_a(addr_a3),  .din_a(din_a3),  .clk_b(clk_b3),  .addr_b(addr_b3),  .dout_b(dout_b3));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram4  (.clk_a(clk_a4),  .we_a(we_a4),  .addr_a(addr_a4),  .din_a(din_a4),  .clk_b(clk_b4),  .addr_b(addr_b4),  .dout_b(dout_b4));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram5  (.clk_a(clk_a5),  .we_a(we_a5),  .addr_a(addr_a5),  .din_a(din_a5),  .clk_b(clk_b5),  .addr_b(addr_b5),  .dout_b(dout_b5));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram6  (.clk_a(clk_a6),  .we_a(we_a6),  .addr_a(addr_a6),  .din_a(din_a6),  .clk_b(clk_b6),  .addr_b(addr_b6),  .dout_b(dout_b6));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram7  (.clk_a(clk_a7),  .we_a(we_a7),  .addr_a(addr_a7),  .din_a(din_a7),  .clk_b(clk_b7),  .addr_b(addr_b7),  .dout_b(dout_b7));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram8  (.clk_a(clk_a8),  .we_a(we_a8),  .addr_a(addr_a8),  .din_a(din_a8),  .clk_b(clk_b8),  .addr_b(addr_b8),  .dout_b(dout_b8));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram9  (.clk_a(clk_a9),  .we_a(we_a9),  .addr_a(addr_a9),  .din_a(din_a9),  .clk_b(clk_b9),  .addr_b(addr_b9),  .dout_b(dout_b9));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram10 (.clk_a(clk_a10), .we_a(we_a10), .addr_a(addr_a10), .din_a(din_a10), .clk_b(clk_b10), .addr_b(addr_b10), .dout_b(dout_b10));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram11 (.clk_a(clk_a11), .we_a(we_a11), .addr_a(addr_a11), .din_a(din_a11), .clk_b(clk_b11), .addr_b(addr_b11), .dout_b(dout_b11));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram12 (.clk_a(clk_a12), .we_a(we_a12), .addr_a(addr_a12), .din_a(din_a12), .clk_b(clk_b12), .addr_b(addr_b12), .dout_b(dout_b12));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram13 (.clk_a(clk_a13), .we_a(we_a13), .addr_a(addr_a13), .din_a(din_a13), .clk_b(clk_b13), .addr_b(addr_b13), .dout_b(dout_b13));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram14 (.clk_a(clk_a14), .we_a(we_a14), .addr_a(addr_a14), .din_a(din_a14), .clk_b(clk_b14), .addr_b(addr_b14), .dout_b(dout_b14));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram15 (.clk_a(clk_a15), .we_a(we_a15), .addr_a(addr_a15), .din_a(din_a15), .clk_b(clk_b15), .addr_b(addr_b15), .dout_b(dout_b15));

endmodule
