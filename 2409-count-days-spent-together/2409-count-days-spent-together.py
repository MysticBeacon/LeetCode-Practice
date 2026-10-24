class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        def get_day(date):
            month = int(date[:2])
            day = int(date[3:])

            return sum(days_in_month[:month - 1]) + day

        alice_start = get_day(arriveAlice)
        alice_end = get_day(leaveAlice)
        bob_start = get_day(arriveBob)
        bob_end = get_day(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)