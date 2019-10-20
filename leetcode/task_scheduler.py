from typing import List
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = defaultdict()
