#####################################################################
# Test DSP mode: mult_12x10
#####################################################################
import random
import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_mult_4x4(dut):
    ################################################################

    rand_vectors = 1000
    nbits_A = 4
    nbits_B = 4
    # Test 10 random vectors
    for test in range(rand_vectors):
        dut._log.info("======== BEGIN Test %d ========", test)
        ################################################################
        # Test the outputs of each 14x10 multiplier
        A = random.randint(0, pow(2, nbits_A) - 1)
        B = random.randint(0, pow(2, nbits_B) - 1)
        dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
        dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

        await Timer(1, units="ns")
        dut._log.info("A is %d", dut.A.value)
        dut._log.info("B is %d", dut.B.value)

        # Calculate expected values of output
        expected_out = dut.A.value.integer * dut.B.value.integer

        dut._log.info("expected_out is %d", expected_out)
        dut._log.info("Actual %d", dut.Y.value)
        assert dut.Y.value == expected_out, "Y does not match expected value!"
        dut._log.info("======== END Test %d ========", test)

    # Test Corner Cases
    ################################################################
    test_id = rand_vectors
    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = pow(2, nbits_A) - 1
    B = pow(2, nbits_B) - 1
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1

    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = 0
    B = 0
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1

    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = pow(2, nbits_A) - 1
    B = random.randint(0, pow(2, nbits_B) - 1)
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1

    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = random.randint(0, pow(2, nbits_A) - 1)
    B = pow(2, nbits_B) - 1
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1

    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = 0
    B = pow(2, nbits_B) - 1
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1

    dut._log.info("======== BEGIN Test %d ========", test_id)
    A = pow(2, nbits_A) - 1
    B = 0
    dut.A.value = BinaryValue(A, n_bits=nbits_A, bigEndian=False)
    dut.B.value = BinaryValue(B, n_bits=nbits_B, bigEndian=False)

    await Timer(1, units="ns")
    dut._log.info("A is %d", dut.A.value)
    dut._log.info("B is %d", dut.B.value)

    # Calculate expected values of output
    expected_out = dut.A.value.integer * dut.B.value.integer
    dut._log.info("expected_out is %d", expected_out)

    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)
    test_id += 1
