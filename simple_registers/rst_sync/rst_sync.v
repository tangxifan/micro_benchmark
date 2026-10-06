module rst_sync (
    input  wire clk,
    input  wire arst,
    output wire srst
);

    reg [1:0] sync_ff;

    always @(posedge clk or posedge arst) begin
        if (arst)
            sync_ff <= 2'b11;       // Asynchronous assertion
        else
            sync_ff <= {sync_ff[0], 1'b0}; // Synchronous de-assertion
    end

    assign srst = sync_ff[1];

endmodule
