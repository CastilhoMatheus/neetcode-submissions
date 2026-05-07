class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let mySet = new Set()

        for (let i = 0; i < nums.length; i++) {
            if (!mySet[nums[i]]) {
                mySet.add(nums[i])
            }
        }
        if (mySet.size != nums.length) {
            return true
        } else {
            return false
        }
    }
}
