///////////////////////////////////////////
// Functionality: 16-Clock Domain 256x16 Dual-Port RAM Array
///////////////////////////////////////////

module dual_port_ram_8x16_mif_16clk #(
    parameter RAM_INIT_FILE = "ram.mif"
)(
    input [15:0] clk_a,
    input [15:0] we_a,
    input [127:0] addr_a,
    input [255:0] din_a,
    
    input [15:0] clk_b,
    input [127:0] addr_b,
    output [255:0] dout_b
);

    dual_port_ram_8x16_mif_Nclk #(
        .N(16),
        .RAM_INIT_FILE(RAM_INIT_FILE)
    ) core (
        .clk_a(clk_a),
        .we_a(we_a),
        .addr_a(addr_a),
        .din_a(din_a),
        .clk_b(clk_b),
        .addr_b(addr_b),
        .dout_b(dout_b)
    );

endmodule
