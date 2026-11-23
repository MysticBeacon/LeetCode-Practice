
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:

        if num == 0:
            # Reset prefix products when zero appears
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:

        # If k is greater than or equal to the
        # number of elements since the last zero
        if k >= len(self.prefix):
            return 0

        # Calculate product using prefix products
        return self.prefix[-1] // self.prefix[-k - 1]
