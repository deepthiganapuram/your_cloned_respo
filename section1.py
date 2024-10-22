1. from typing import Dict, List
   import pandas as pd
   def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
       return [elem for i in range(0, len(lst), n) for elem in reversed(lst[i:i + n])]
   lst = list(map(int, input().split()))
   n = int(input())
   result = reverse_by_n_elements(lst, n)
   print(result)

2. from typing import List, Dict

    def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
         grouped_dict = {}
        for string in lst:
            length = len(string)
            if length not in grouped_dict:
                grouped_dict[length] = []
        grouped_dict[length].append(string)
    
    return grouped_dict
lst = list(map(int, input().split()))
result = group_by_length(lst)
print(result)

3.  def _flatten(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
        items = []
        for key, value in d.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key  # Combine keys with separator
            if isinstance(value, dict):  # If value is a dict, recurse
                items.extend(_flatten(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)
    
    return _flatten(nested_dict, sep=sep)

4.def unique_permutations(nums: List[int]) -> List[List[int]]:
    def backtrack(first: int):
        if first == len(nums):
            result.append(nums[:]) 
            seen = set()  
        for i in range(first, len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
    
    result = []
    nums.sort()  # Sort the numbers to ensure uniqueness handling
    backtrack(0)
    return result

5. def find_all_dates(text: str) -> List[str]:
     date_pattern = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\
     dates = re.findall(date_pattern, text) 
    return dates

6.  def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    coordinates = polyline.decode(polyline_str)
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    return df
polyline_str = 'u{~vFvyys@fApCz@hBd@b@zAj@`Bb@vAhAvBdAfB'
df = polyline_to_dataframe(polyline_str)
print(df)

7.  def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
         num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    rotated_matrix = [[matrix[num_rows - 1 - j][i] for j in range(num_rows)] for i in range(num_cols)]
    for i in range(num_cols):
        for j in range(num_rows):
            original_row = num_rows - 1 - j
            original_col = i
            rotated_matrix[i][j] *= (original_row + original_col)
    return rotated_matrix
result = rotate_and_multiply_matrix(matrix)
for row in result:
    print(row)

8.def time_check(df: pd.DataFrame) -> pd.Series:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    grouped = df.groupby(['id', 'id_2'])
    def check_time_period(group: pd.DataFrame) -> bool:
        time_span = group['timestamp'].max() - group['timestamp'].min()
        return time_span >= pd.Timedelta(days=7) and len(group) >= 24
    result = grouped.apply(check_time_period)
    return result
df = pd.DataFrame(data)
result = time_check(df)
print(result)




