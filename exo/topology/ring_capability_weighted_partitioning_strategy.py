from typing import List
from .partitioning_strategy import PartitioningStrategy
from .topology import Topology
from .partitioning_strategy import Partition

class RingCapabilityWeightedPartitioningStrategy(PartitioningStrategy):
  def partition(self, topology: Topology) -> List[Partition]:
    nodes = list(topology.all_nodes())
    nodes.sort(key=lambda x: (x[1].memory, x[0]), reverse=True)
    total_memory = sum(node[1].memory for node in nodes)
    partitions = []
    start = 0
    for node in nodes:
      end = round(start + (node[1].memory/total_memory), 5)
      partitions.append(Partition(node[0], start, end))
      start = end
    return partitions
  
def packKnapSack(W, wt, val, n):
  dp = [0 for i in range(W+1)]
  for i in range(1, n+1):
    for w in range(W, 0, -1):
      if wt[i-1] <= w:
        dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1])
  return dp[W]
