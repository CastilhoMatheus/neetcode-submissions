class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalDamage = sum(damage)

        if armor == 0:
            return totalDamage + 1
        
        return totalDamage - min(max(damage), armor) + 1