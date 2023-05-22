class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """freqs = dict()
        for i in range(len(nums)):
            if nums[i] in freqs:
                freqs[nums[i]] += 1
            else:
                freqs[nums[i]] = 1
        sorted_values = sorted(freqs.values())[::-1][:k]
        solution = []
        for val in sorted_values:
            for key in freqs.keys():
                if freqs[key] == val and key not in solution:
                    solution.append(key)
                    # O(n^2) unfortunately
        return solution  """

        freqs = dict()
        for i in range(len(nums)):
            # O(n)
            if nums[i] in freqs:
                freqs[nums[i]] += 1
            else:
                freqs[nums[i]] = 1
        rev_freqs = dict()
        for key in freqs.keys():
            # O(n)
            if freqs[key] in rev_freqs:
                rev_freqs[freqs[key]].append(key)
            else:
                rev_freqs[freqs[key]] = [key]
        sorted_keys = sorted(rev_freqs.keys())[::-1]
        # O(n log n)
        solution = []
        for key in sorted_keys:
            # O(n)
            solution.extend(rev_freqs[key])
        return solution[:k]
            