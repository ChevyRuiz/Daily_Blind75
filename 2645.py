class Solution:
    def addMinimum(self, word: str) -> int:
        sequence = ["a", "b", "c"]
        count = 0
        seqIndex = 0
        for letter in word:
            while letter != sequence[seqIndex]:
                count += 1
                seqIndex = (seqIndex + 1) % 3
            seqIndex = (seqIndex + 1) % 3  
        if sequence[seqIndex] == "c":
            count += 1
        elif sequence[seqIndex] == "b":
            count += 2
        return count
