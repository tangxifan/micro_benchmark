module rstn_sync (
    input  wire clk,
    input  wire arst_n,      // Asynchronous active-low reset
    output wire srst_n       // Synchronized reset
);

    reg [1:0] sync_ff;

    always @(posedge clk or negedge arst_n) begin
        if (!arst_n)
            sync_ff <= 2'b00;       // Asynchronously assert reset
        else
            sync_ff <= {sync_ff[0], 1'b1}; // Synchronously release reset
    end

    assign srst_n = sync_ff[1];

endmodule
