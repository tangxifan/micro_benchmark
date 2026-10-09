///////////////////////////////////////////
//  Functionality: 32-Clock Dual-Port RAM (8x16) Hierarchical Wrapper with Flattened Ports
//  Author:        Xifan Tang
////////////////////////////////////////

module dual_port_ram_8x16_mif_32clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input  wire        clk_a0,  input  wire        clk_a1,  input  wire        clk_a2,  input  wire        clk_a3,
    input  wire        clk_a4,  input  wire        clk_a5,  input  wire        clk_a6,  input  wire        clk_a7,
    input  wire        clk_a8,  input  wire        clk_a9,  input  wire        clk_a10, input  wire        clk_a11,
    input  wire        clk_a12, input  wire        clk_a13, input  wire        clk_a14, input  wire        clk_a15,
    input  wire        clk_a16, input  wire        clk_a17, input  wire        clk_a18, input  wire        clk_a19,
    input  wire        clk_a20, input  wire        clk_a21, input  wire        clk_a22, input  wire        clk_a23,
    input  wire        clk_a24, input  wire        clk_a25, input  wire        clk_a26, input  wire        clk_a27,
    input  wire        clk_a28, input  wire        clk_a29, input  wire        clk_a30, input  wire        clk_a31,
    input  wire        we_a0,   input  wire        we_a1,   input  wire        we_a2,   input  wire        we_a3,
    input  wire        we_a4,   input  wire        we_a5,   input  wire        we_a6,   input  wire        we_a7,
    input  wire        we_a8,   input  wire        we_a9,   input  wire        we_a10,  input  wire        we_a11,
    input  wire        we_a12,  input  wire        we_a13,  input  wire        we_a14,  input  wire        we_a15,
    input  wire        we_a16,  input  wire        we_a17,  input  wire        we_a18,  input  wire        we_a19,
    input  wire        we_a20,  input  wire        we_a21,  input  wire        we_a22,  input  wire        we_a23,
    input  wire        we_a24,  input  wire        we_a25,  input  wire        we_a26,  input  wire        we_a27,
    input  wire        we_a28,  input  wire        we_a29,  input  wire        we_a30,  input  wire        we_a31,
    input  wire [7:0]  addr_a0, input  wire [7:0]  addr_a1, input  wire [7:0]  addr_a2, input  wire [7:0]  addr_a3,
    input  wire [7:0]  addr_a4, input  wire [7:0]  addr_a5, input  wire [7:0]  addr_a6, input  wire [7:0]  addr_a7,
    input  wire [7:0]  addr_a8, input  wire [7:0]  addr_a9, input  wire [7:0]  addr_a10,input  wire [7:0]  addr_a11,
    input  wire [7:0]  addr_a12,input  wire [7:0]  addr_a13,input  wire [7:0]  addr_a14,input  wire [7:0]  addr_a15,
    input  wire [7:0]  addr_a16,input  wire [7:0]  addr_a17,input  wire [7:0]  addr_a18,input  wire [7:0]  addr_a19,
    input  wire [7:0]  addr_a20,input  wire [7:0]  addr_a21,input  wire [7:0]  addr_a22,input  wire [7:0]  addr_a23,
    input  wire [7:0]  addr_a24,input  wire [7:0]  addr_a25,input  wire [7:0]  addr_a26,input  wire [7:0]  addr_a27,
    input  wire [7:0]  addr_a28,input  wire [7:0]  addr_a29,input  wire [7:0]  addr_a30,input  wire [7:0]  addr_a31,
    input  wire [15:0] din_a0,  input  wire [15:0] din_a1,  input  wire [15:0] din_a2,  input  wire [15:0] din_a3,
    input  wire [15:0] din_a4,  input  wire [15:0] din_a5,  input  wire [15:0] din_a6,  input  wire [15:0] din_a7,
    input  wire [15:0] din_a8,  input  wire [15:0] din_a9,  input  wire [15:0] din_a10, input  wire [15:0] din_a11,
    input  wire [15:0] din_a12, input  wire [15:0] din_a13, input  wire [15:0] din_a14, input  wire [15:0] din_a15,
    input  wire [15:0] din_a16, input  wire [15:0] din_a17, input  wire [15:0] din_a18, input  wire [15:0] din_a19,
    input  wire [15:0] din_a20, input  wire [15:0] din_a21, input  wire [15:0] din_a22, input  wire [15:0] din_a23,
    input  wire [15:0] din_a24, input  wire [15:0] din_a25, input  wire [15:0] din_a26, input  wire [15:0] din_a27,
    input  wire [15:0] din_a28, input  wire [15:0] din_a29, input  wire [15:0] din_a30, input  wire [15:0] din_a31,
    
    input  wire        clk_b0,  input  wire        clk_b1,  input  wire        clk_b2,  input  wire        clk_b3,
    input  wire        clk_b4,  input  wire        clk_b5,  input  wire        clk_b6,  input  wire        clk_b7,
    input  wire        clk_b8,  input  wire        clk_b9,  input  wire        clk_b10, input  wire        clk_b11,
    input  wire        clk_b12, input  wire        clk_b13, input  wire        clk_b14, input  wire        clk_b15,
    input  wire        clk_b16, input  wire        clk_b17, input  wire        clk_b18, input  wire        clk_b19,
    input  wire        clk_b20, input  wire        clk_b21, input  wire        clk_b22, input  wire        clk_b23,
    input  wire        clk_b24, input  wire        clk_b25, input  wire        clk_b26, input  wire        clk_b27,
    input  wire        clk_b28, input  wire        clk_b29, input  wire        clk_b30, input  wire        clk_b31,
    input  wire [7:0]  addr_b0, input  wire [7:0]  addr_b1, input  wire [7:0]  addr_b2, input  wire [7:0]  addr_b3,
    input  wire [7:0]  addr_b4, input  wire [7:0]  addr_b5, input  wire [7:0]  addr_b6, input  wire [7:0]  addr_b7,
    input  wire [7:0]  addr_b8, input  wire [7:0]  addr_b9, input  wire [7:0]  addr_b10,input  wire [7:0]  addr_b11,
    input  wire [7:0]  addr_b12,input  wire [7:0]  addr_b13,input  wire [7:0]  addr_b14,input  wire [7:0]  addr_b15,
    input  wire [7:0]  addr_b16,input  wire [7:0]  addr_b17,input  wire [7:0]  addr_b18,input  wire [7:0]  addr_b19,
    input  wire [7:0]  addr_b20,input  wire [7:0]  addr_b21,input  wire [7:0]  addr_b22,input  wire [7:0]  addr_b23,
    input  wire [7:0]  addr_b24,input  wire [7:0]  addr_b25,input  wire [7:0]  addr_b26,input  wire [7:0]  addr_b27,
    input  wire [7:0]  addr_b28,input  wire [7:0]  addr_b29,input  wire [7:0]  addr_b30,input  wire [7:0]  addr_b31,
    output wire [15:0] dout_b0, output wire [15:0] dout_b1, output wire [15:0] dout_b2, output wire [15:0] dout_b3,
    output wire [15:0] dout_b4, output wire [15:0] dout_b5, output wire [15:0] dout_b6, output wire [15:0] dout_b7,
    output wire [15:0] dout_b8, output wire [15:0] dout_b9, output wire [15:0] dout_b10,output wire [15:0] dout_b11,
    output wire [15:0] dout_b12,output wire [15:0] dout_b13,output wire [15:0] dout_b14,output wire [15:0] dout_b15,
    output wire [15:0] dout_b16,output wire [15:0] dout_b17,output wire [15:0] dout_b18,output wire [15:0] dout_b19,
    output wire [15:0] dout_b20,output wire [15:0] dout_b21,output wire [15:0] dout_b22,output wire [15:0] dout_b23,
    output wire [15:0] dout_b24,output wire [15:0] dout_b25,output wire [15:0] dout_b26,output wire [15:0] dout_b27,
    output wire [15:0] dout_b28,output wire [15:0] dout_b29,output wire [15:0] dout_b30,output wire [15:0] dout_b31
);

    // Instantiate Instances 0 to 31
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
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram16 (.clk_a(clk_a16), .we_a(we_a16), .addr_a(addr_a16), .din_a(din_a16), .clk_b(clk_b16), .addr_b(addr_b16), .dout_b(dout_b16));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram17 (.clk_a(clk_a17), .we_a(we_a17), .addr_a(addr_a17), .din_a(din_a17), .clk_b(clk_b17), .addr_b(addr_b17), .dout_b(dout_b17));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram18 (.clk_a(clk_a18), .we_a(we_a18), .addr_a(addr_a18), .din_a(din_a18), .clk_b(clk_b18), .addr_b(addr_b18), .dout_b(dout_b18));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram19 (.clk_a(clk_a19), .we_a(we_a19), .addr_a(addr_a19), .din_a(din_a19), .clk_b(clk_b19), .addr_b(addr_b19), .dout_b(dout_b19));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram20 (.clk_a(clk_a20), .we_a(we_a20), .addr_a(addr_a20), .din_a(din_a20), .clk_b(clk_b20), .addr_b(addr_b20), .dout_b(dout_b20));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram21 (.clk_a(clk_a21), .we_a(we_a21), .addr_a(addr_a21), .din_a(din_a21), .clk_b(clk_b21), .addr_b(addr_b21), .dout_b(dout_b21));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram22 (.clk_a(clk_a22), .we_a(we_a22), .addr_a(addr_a22), .din_a(din_a22), .clk_b(clk_b22), .addr_b(addr_b22), .dout_b(dout_b22));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram23 (.clk_a(clk_a23), .we_a(we_a23), .addr_a(addr_a23), .din_a(din_a23), .clk_b(clk_b23), .addr_b(addr_b23), .dout_b(dout_b23));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram24 (.clk_a(clk_a24), .we_a(we_a24), .addr_a(addr_a24), .din_a(din_a24), .clk_b(clk_b24), .addr_b(addr_b24), .dout_b(dout_b24));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram25 (.clk_a(clk_a25), .we_a(we_a25), .addr_a(addr_a25), .din_a(din_a25), .clk_b(clk_b25), .addr_b(addr_b25), .dout_b(dout_b25));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram26 (.clk_a(clk_a26), .we_a(we_a26), .addr_a(addr_a26), .din_a(din_a26), .clk_b(clk_b26), .addr_b(addr_b26), .dout_b(dout_b26));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram27 (.clk_a(clk_a27), .we_a(we_a27), .addr_a(addr_a27), .din_a(din_a27), .clk_b(clk_b27), .addr_b(addr_b27), .dout_b(dout_b27));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram28 (.clk_a(clk_a28), .we_a(we_a28), .addr_a(addr_a28), .din_a(din_a28), .clk_b(clk_b28), .addr_b(addr_b28), .dout_b(dout_b28));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram29 (.clk_a(clk_a29), .we_a(we_a29), .addr_a(addr_a29), .din_a(din_a29), .clk_b(clk_b29), .addr_b(addr_b29), .dout_b(dout_b29));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram30 (.clk_a(clk_a30), .we_a(we_a30), .addr_a(addr_a30), .din_a(din_a30), .clk_b(clk_b30), .addr_b(addr_b30), .dout_b(dout_b30));
    dual_port_ram_8x16_mif #(.RAM_INIT_FILE(RAM_INIT_FILE)) u_ram31 (.clk_a(clk_a31), .we_a(we_a31), .addr_a(addr_a31), .din_a(din_a31), .clk_b(clk_b31), .addr_b(addr_b31), .dout_b(dout_b31));

endmodule
