
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):

        count = 0

        for i in arr1:

            valid = True

            for j in arr2:

                if abs(i - j) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count
