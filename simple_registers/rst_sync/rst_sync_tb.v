`timescale 1ns/1ps

module rst_sync_tb;

    reg  clk;
    reg  arst;
    wire srst;

    integer errors;

    // ============================================================
    // DUT
    // ============================================================
    rst_sync dut (
        .clk  (clk),
        .arst (arst),
        .srst (srst)
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
            if (srst !== expected) begin
                $display("ERROR: time=%0t | arst=%b | srst=%b | expected=%b",
                         $time, arst, srst, expected);
                errors = errors + 1;
            end
            else begin
                $display("PASS : time=%0t | arst=%b | srst=%b",
                         $time, arst, srst);
            end
        end
    endtask

    // ============================================================
    // Test
    // ============================================================
    initial begin
        errors = 0;

        $display("==========================================");
        $display(" Active-High Reset Synchronizer Test");
        $display("==========================================");

        // --------------------------------------------------------
        // Test 1: Assert reset
        // --------------------------------------------------------
        arst = 1'b1;

        #1;

        // Reset must assert asynchronously
        check_reset(1'b1);

        // --------------------------------------------------------
        // Test 2: De-assert reset
        // --------------------------------------------------------
        arst = 1'b0;

        #1;

        // Output must remain asserted
        check_reset(1'b1);

        // First rising edge
        @(posedge clk);
        #1;
        check_reset(1'b1);

        // Second rising edge
        @(posedge clk);
        #1;
        check_reset(1'b0);

        // --------------------------------------------------------
        // Test 3: Assert reset between clock edges
        // --------------------------------------------------------
        #2;
        arst = 1'b1;

        #1;

        // Must assert immediately
        check_reset(1'b1);

        // --------------------------------------------------------
        // Test 4: De-assert again
        // --------------------------------------------------------
        arst = 1'b0;

        #1;

        // Must remain asserted
        check_reset(1'b1);

        @(posedge clk);
        #1;
        check_reset(1'b1);

        @(posedge clk);
        #1;
        check_reset(1'b0);

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
