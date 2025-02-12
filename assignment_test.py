import unittest
import numpy as np
import pandas as pd

    
# Task 1: NumPy Basics
# 1.
def test_numpy_array_creation(arr):
    expected = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    np.testing.assert_array_equal(arr, expected)

# 2.
def test_numpy_matrix_creation(matrix):
    assert matrix.shape == (5, 5), "Array shape is incorrect"
    assert 0 <= matrix.min() <= 10 and 0 <= matrix.max() <= 10, "Array values are out of bounds"


# 3.
def test_numpy_operations(addition, subtraction, division, multiplication):
    np.testing.assert_array_equal(addition, np.array([[43,66,14], [13,48,55], [94,41,27]]))
    np.testing.assert_array_equal(subtraction, np.array([[39,8,6], [-7,22,37], [-2,-23,13]]))
    np.testing.assert_array_equal(division, np.array([[20.5,1.27586207,2.5], [0.3,2.69230769,5.11111111], [0.95833333,0.28125,2.85714286]]))
    np.testing.assert_array_equal(multiplication, np.array([[82,1073,40], [30,455,414], [2208,288,140]]))

# 4.
def test_numpy_slicing(sliced):
    expected = np.array([300, 400, 500, 600, 700])
    np.testing.assert_array_equal(sliced, expected)

# 5.
def test_numpy_methods(arr, add, average, max):
    
    assert arr.shape == (3, 3), "Array shape is incorrect"
    #
    expected_sum = 270
    expected_average = 30
    expected_max = 46
    np.testing.assert_array_equal(add, expected_sum)
    np.testing.assert_array_equal(average, expected_average)
    np.testing.assert_array_equal(max, expected_max) 


# Task 2: Pandas Basics
# 1.
def test_pandas_series_creation(series):
    assert series['i'] == 100
    assert series['ii'] == 500

# 2.
def test_dataframe_reading_and_manipulation(df, filtered_df):
    assert df.loc[0, 'Tax'] == 10978.95
    assert df.loc[1, 'Tax'] == 12809.70
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['Name'] == "Bob"

# 3.
def test_dataframe_aggregation(total_sales):
    assert total_sales["North"] == 2700
    assert total_sales["South"] == 2800

# 4.
def test_dataframe_merging(merged):
    assert len(merged) == 4
    assert "OrderID" in merged.columns

# 5.
def test_dataframe_pivot_table(pivot_table):
    assert pivot_table.loc["North", "P"] == 250
    assert pivot_table.loc["South", "Q"] == 200

if __name__ == "__main__":
    # call the function