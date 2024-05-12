import pyperf

import main

def bench():
    runner = pyperf.Runner()

    runner.timeit(name="bitstr",
                  stmt="bitstr_inv_sqrt(x)",
                  setup="""
import random
                  
x = random.uniform(0.01, 1000)
""",
                  globals={"bitstr_inv_sqrt": main.bitstr_inv_sqrt})

    runner.timeit(name="struct",
                  stmt="struct_inv_sqrt(x)",
                  setup="""
import random

x = random.uniform(0.01, 1000)
                  """,
                  globals={"struct_inv_sqrt": main.struct_inv_sqrt})


if __name__ == "__main__":
    bench()
