import subprocess
def main():
    
    with open('input.txt', 'r') as input_file:
        input_data = input_file.read().strip()

    process = subprocess.Popen(
        ['python', 'main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = process.communicate(input=input_data)
 
    if stderr:
        print(f"Error: {stderr}")
        return

    with open('output.txt') as file:
        output = file.read()

    answers = output.strip().split('\n')
    output = stdout.strip().split('\n')

    answer_lines, output_lines = len(answers), len(output)

    if answer_lines != output_lines:
        print(f"Your output is {output_lines} lines, but the expected is {answer_lines} lines.")
        return

    passed = 0
    for i in range(answer_lines):
        expected, found = answers[i], output[i]
        if expected == found:
            passed += 1
        else:
            print(f"Output line #{i+1}\nExpected: {expected}\nFound: {found}\n")
    if passed == answer_lines:
        print('All tests Passed')
    else:
        print(f'{passed}/{answer_lines} tests Passed')


main()