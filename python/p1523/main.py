class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num_odds = (high - low) // 2
        if low % 2 == 1:
            num_odds += 1
        return num_odds
