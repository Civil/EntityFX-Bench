from entityfx import benchmark, benchmark_base, writer
from entityfx.arithemtics_benchmark import ArithemticsBenchmark
from entityfx.math_benchmark import MathBenchmark
from entityfx.writer import Writer

import time

writer = Writer(None)

benchmark_base.BenchmarkBase.ITERRATIONS_RATIO = 0.01

def write_result(bench_result) -> None:
    writer.write_title("{0:<30}", bench_result["Name"])
    writer.write_value("{0:>13.2f} ms", bench_result["Elapsed"])
    writer.write_value("{0:>13.2f} pts", bench_result["Points"])
    writer.write_value("{0:>13.2f} {1}", bench_result["Result"], bench_result["Units"])
    writer.write_line()
    writer.write_value("Iterrations: {0:<15}, Ratio: {1:<15}", bench_result["Iterrations"], bench_result["Ratio"])
    writer.write_line()


bench_marks = [
    ArithemticsBenchmark(), 
    MathBenchmark(), 
    # CallBenchmark(), 
    # IfElseBenchmark(), 
    # StringManipulation(),  
    # MemoryBenchmark(), 
    # RandomMemoryBenchmark(), 
    # Scimark2Benchmark(), 
    # DhrystoneBenchmark(), 
    # WhetstoneBenchmark(), 
    # LinpackBenchmark(), 
    ]


total = 0
total_points = 0

result = list()

writer.write_header("Warmup")

for bench in bench_marks: 
    bench.warmup(.05)
    writer.write(".")

writer.write_line()
writer.write_header("Bench")

i = 1
for bench in bench_marks: 
    writer.write_header("[{0}] {1}", i, bench.name)
    r = bench.bench()
    total += r["Elapsed"]
    total_points += r["Points"]
    write_result(r)
    result.append(r)
    i += 1
       
