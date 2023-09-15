import numpy as np

class EucsContext:

    def __init__(self, no_of_dimensions: int, distribution: str = "flat"):
        self.rng = np.random.default_rng(67634125) # This is a random deterministic generation using keyboard mashing seed generation technique
        self.no_of_dimensions = no_of_dimensions
        self.data_size = 0
        self.no_of_queries = 0
        self.no_of_ref_points = 0
        self.distribution = distribution

    def set_sizes(self, data_size: int, no_of_queries: int, no_of_ref_points: int, no_of_witnesses: int):
        self.data_size = data_size
        self.no_of_queries = no_of_queries
        self.no_of_ref_points = no_of_ref_points
        self.no_of_witnesses = no_of_witnesses

    def get_data(self) -> np.array:
        return self._generate(self.data_size)

    def get_ref_points(self) -> np.array:
        return self._generate(self.no_of_ref_points)

    def get_queries(self) -> np.array:
        return self._generate(self.no_of_queries)

    def get_witnesses(self) -> np.array:
        return self._generate(self.no_of_witnesses)

    def _generate(self, rows: int) -> np.array:
        assert self.no_of_dimensions != 0
        assert rows > 0
        if self.distribution == "flat":
            return self.rng.uniform(0, 1, (rows, self.no_of_dimensions)).astype("float32")              # uniform distribution
        elif self.distribution == "gauss":
            return self.rng.normal(0.5, 0.2625, (rows, self.no_of_dimensions)).astype("float32")           # gaussian distribution
            # This gives some negatives - should we clip the data to the unit cube.
            # The value of 0.2625 gives 119 hits for 100 000 000 at threshold of 0.6017
        else:
            raise ValueError('Distribution argument to constructor must be either "flat" (default) or "gauss"')



