"""
steps:
1.copy the given input into sample_in.txt
2.copy the expected output for the sample testcases to sample_out.txt
3.your solution should be written in a format specified in solution.py
4.use find and replace shortcut to convert from "input" to "data.readline"
5. for each test case(the for loop on the bottom), assign answers.readline() to a variable(e.g "expected")
6. compare the expected result with your output and debug the result.
7.Think for a moment and go to site and submit the "SOLUTION.PY"
"""
"""DO NOT FORGET TO USE CAST OPERATORS AND STRIP THE INPUT OFF WHITESPACE CHARACTERS WHEN NECESSARY"""

data = open("sample_in.txt")
answers = open("sample_out.txt")


"""your function should process a single test case"""


def write_a_solution_for_a_single_test_case():
    """
    :return should return the expected output: 
    """
    return "the expected output for this test case."


number_of_test_cases = int(input())
for test_num in range(number_of_test_cases):
    output = write_a_solution_for_a_single_test_case()
    expected = cast(answers.readline()) #DO NOT Forget to cast expected output since it only outputs strings.
    if output == expected:
        print(f"passed test{test_num")
    else:
        print(f"failed test{test_num} expected: {expected}, output: {output}")
    
data.close()
answers.close()
