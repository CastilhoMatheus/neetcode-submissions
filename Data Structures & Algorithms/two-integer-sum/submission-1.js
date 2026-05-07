class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map();

        for (let i = 0; i < nums.length; i++) {
            const searchVal = target - nums[i];

            if (map.has(searchVal)) {
                return [map.get(searchVal), i];
            }
            map.set(nums[i], i);
        }
        return [];
    }
}
