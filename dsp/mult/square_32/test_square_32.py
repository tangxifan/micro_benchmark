#####################################################################
# Test a 32-bit combinatorial square: square_32
#####################################################################
import random
import cocotb
from cocotb.types import LogicArray
from cocotb.triggers import Timer

NBITS = 32


async def check_square(dut, test_id, A):
    dut._log.info("======== BEGIN Test %d ========", test_id)
    dut.A.value = LogicArray(A, NBITS)

    await Timer(1, "ns")
    dut._log.info("A is %d", dut.A.value)

    # Calculate expected values of output
    expected_out = A * A
    dut._log.info("expected_out is %d", expected_out)
    dut._log.info("Actual %d", dut.Y.value)
    assert dut.Y.value == expected_out, "Y does not match expected value!"
    dut._log.info("======== END Test %d ========", test_id)


@cocotb.test()
async def test_square_32(dut):
    max_value = pow(2, NBITS) - 1
    # Random vectors
    vectors = [random.randint(0, max_value) for _ in range(1000)]
    # Corner cases
    vectors += [max_value, 0, 1]
    for test_id, A in enumerate(vectors):
        await check_square(dut, test_id, A)
