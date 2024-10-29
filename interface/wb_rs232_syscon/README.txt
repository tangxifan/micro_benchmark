README.TXT -- For risc16f84.v

Author:  John Clayton
Date  :  August 8, 2003


This is a very short description of the files given in the distribution .zip file.

All of the .v files are verilog source code.
The top level of the hierarchy is called "top.v"
The reg_8_iorw_clrset.v file is the registers (instantiates "reg_8_io_clrset.v")
The processor is "risc16f84_clk2x.v" -- It is all contained in ONE FILE.
The serial hardware debugger is "rs232_syscon.v" -- SEE RELATED OPENCORES PROJECT
                                                    FOR MORE DETAILS
The serial ports are in serial.v
The BAUD rate generator is "auto_baud_with_tracking.v" -- SEE RELATED OPENCORES PROJECT
The vga_128_by_92.v file is used for generating large, block shaped "pixels" which 
    are really 5 by 5 pixels in size, on a flat panel display.  The display is from
    an IBM thinkpad 700C laptop computer, ancient but it works.  This unit can easily
    be removed from the design for those who don't want it, which is probably almost
    everyone!
All of the "bugcheck" or "bugche~1" files are the C-code which I used to check for some
    bugs which were recently reported by some users.  It shows examples of interrupts
    being used.  It was compiled with the PICC "pcw.exe" compiler, 1997 version.
The Perl script "srec_to_rs232.pl" converts S-record files (in this case BUGCHE~1.HEX)
    into commands for the hardware debugger.  The resulting file, bugche~1.232 can be
    sent as a text file serially to the debugger, and it will load the code into memory
    by writing each byte as a separate debugger command.  It's slow, but hey, it works.
The constraints file is "pndkr_1e.ucf" -- Modify to your heart's contentment.
The design compiles on Xilinx WEBPACK free tools.
Set the state machine inference setting to "user" under synthesis properties.  That's
    what I always do...  It seems to run better.

Notes on using this design, helpful tips, etc.:

The design can easily be clocked at 50 MHz in a Xilinx XC2S200e or similar FPGA.
The whole debugging environment takes up about 30% of the XC2S200e FPGA.
Xilinx synchronous block RAMs are using instead of asynchronous RAMs.  Because they
   are emulating asynchronous RAMs, they are clocked at twice the speed of the rest
   of the logic.  Use asychronous RAMs if you like, instead of the architecturally
   specific BRAMs.
If you are using Windows hyperterm program and you encounter occasional glitches in
   serial port operation, reduce the speed to 57600 BAUD or lower, and try inserting
   an intercharacter and/or interline delay of 1ms.  Other terminal programs, such as
   securecrt may behave better.
You can use the single stepping and breakpoint logic to help you debug.  For breakpoints
   set the address 2 further than the instruction you want to see completed, and you 
   will see the results written back to registers.  The addresses for using the break
   points are given in the file "top.v"  For instance, the address breakpoint is in
   registers at FF02 and FF03.  Set the full address into these two registers (lsb first!)
   and then enable the address breakpoint by setting FF06 to 01.  This can be done
   while the processor is running, due to the dual-port nature of the block RAMs.
You can start the processor running code by issuing this command:  w ff0b 02.
You can keep the processor running and start periodic interrupts with this command:
   w ff0b 6.
To halt the processor, issue this command:  w ff0b 00.
You can reset the processor by issuing this command twice:  i.

The processor registers are all visible at 8000 in the memory map.
However, certain registers are really only shadowed there (i.e. if you try to mask
and unmask interrupts by writing to 800b with the debugger, it will not take effect
because the actual interrupt mask bits are contained within the processor, NOT within
the register that shadows the bits.

You can see the values changing in the registers during execution of the processor, it
will not disturb the processor because the memory is DUAL PORTED.

Have fun!!!

