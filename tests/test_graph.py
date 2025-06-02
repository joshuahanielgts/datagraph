import unittest
import os
from datagraph.graph import generate_plot

class TestDataGraph(unittest.TestCase):

    def setUp(self):
        self.csv_path = "sample.csv"
        self.output_path = "test_output.png"
        with open(self.csv_path, "w") as f:
            f.write("Date,Sales,Revenue,Category\n2024-01,100,2000,A\n2024-02,150,2500,B\n2024-03,130,2300,C\n")

    def tearDown(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_line_chart(self):
        generate_plot(self.csv_path, "Date", ["Sales"], "line", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_bar_chart(self):
        generate_plot(self.csv_path, "Date", ["Revenue"], "bar", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_scatter_chart(self):
        generate_plot(self.csv_path, "Date", ["Revenue"], "scatter", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_area_chart(self):
        generate_plot(self.csv_path, "Date", ["Sales"], "area", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_histogram(self):
        generate_plot(self.csv_path, None, ["Sales"], "hist", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_pie_chart(self):
        generate_plot(self.csv_path, None, ["Category"], "pie", self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

if __name__ == "__main__":
    unittest.main()
