from entityfx.scimark2 import Scimark2
from entityfx.benchmark_base import BenchmarkBase
from entityfx.writer import Writer

class ParallelScimark2Benchmark(BenchmarkBase):

    def __init__(self, writer: Writer, print_to_console : bool=True) -> None:
        super().__init__(writer, print_to_console)
        self.is_parallel = True
        self.ratio = 10
    
    def benchImplementation(self) -> list:
        return self.bench_in_parallel(lambda : Scimark2(False), lambda a: a.bench(), lambda a, r : self.setBenchResultFunc(a, r))

    def warmup(self, aspect : float=.05) -> None:
        pass

    def populateResult(self, bench_result, results : list):
        result = self._buildParallelResult(bench_result, results) 
        result["Result"] = sum(map(lambda x : x["Result"], results))
        result["Units"] = "CompositeScore"
        result["Output"] = "".join(map(lambda x : x["Output"], results))
        return result

    def setBenchResultFunc(self, a, r):
        r["Points"] = a["CompositeScore"] * self.ratio
        r["Result"] = a["CompositeScore"]
        r["Output"] = a["Output"]