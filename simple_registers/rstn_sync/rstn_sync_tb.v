`timescale 1ns/1ps

module rstn_sync_tb;

    reg  clk;
    reg  arst_n;
    wire srst_n;

    integer errors;

    // ============================================================
    // DUT
    // ============================================================
    rstn_sync dut (
        .clk    (clk),
        .arst_n (arst_n),
        .srst_n (srst_n)
    );

    // ============================================================
    // Clock: 10 ns period
    // ============================================================
    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    // ============================================================
    // Check task
    // ============================================================
    task check_reset;
        input expected;
        begin
            if (srst_n !== expected) begin
                $display("ERROR: time=%0t | arst_n=%b | srst_n=%b | expected=%b",
                         $time, arst_n, srst_n, expected);
                errors = errors + 1;
            end
            else begin
                $display("PASS : time=%0t | arst_n=%b | srst_n=%b",
                         $time, arst_n, srst_n);
            end
        end
    endtask

    // ============================================================
    // Test
    // ============================================================
    initial begin
        errors = 0;

        $display("==========================================");
        $display(" Active-Low Reset Synchronizer Test");
        $display("==========================================");

        // --------------------------------------------------------
        // Test 1: Assert reset
        // --------------------------------------------------------
        arst_n = 1'b0;

        #1;

        // Reset must assert asynchronously
        check_reset(1'b0);

        // --------------------------------------------------------
        // Test 2: De-assert reset
        // --------------------------------------------------------
        arst_n = 1'b1;

        // Immediately after de-assertion, srst_n
        // must STILL be asserted.
        #1;
        check_reset(1'b0);

        // First rising edge
        @(posedge clk);
        #1;
        check_reset(1'b0);

        // Second rising edge
        @(posedge clk);
        #1;
        check_reset(1'b1);

        // --------------------------------------------------------
        // Test 3: Assert reset between clock edges
        // --------------------------------------------------------
        #2;
        arst_n = 1'b0;

        #1;

        // Must assert immediately
        check_reset(1'b0);

        // --------------------------------------------------------
        // Test 4: De-assert again
        // --------------------------------------------------------
        arst_n = 1'b1;

        #1;

        // Must remain asserted
        check_reset(1'b0);

        @(posedge clk);
        #1;
        check_reset(1'b0);

        @(posedge clk);
        #1;
        check_reset(1'b1);

        // --------------------------------------------------------
        // Final result
        // --------------------------------------------------------
        $display("==========================================");

        if (errors == 0) begin
            $display("TEST PASSED");
        end
        else begin
            $display("TEST FAILED: %0d errors", errors);
        end

        $display("==========================================");

        $finish;
    end

endmodule
