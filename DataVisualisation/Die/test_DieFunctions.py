from DataVisualisation.Die.DieFunctions import input_range, number_sides


class TestDieFunctions:
    def test_default_input_range(self):
        i = input_range('')
        assert i == 1_000_000

    def test_input_range(self):
        i = input_range(100000)
        assert i == 100000

    def test_default_sides(self):
        i = number_sides('')
        assert i == 20

    def test_sides(self):
        i = number_sides(20)
        assert i == 20


