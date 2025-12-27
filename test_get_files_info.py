from functions.get_files_info import get_files_info
# Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True
test_cases = [
    ['calculator', '.'],
    ["calculator", "pkg"],
    ["calculator", "/bin"],
    ["calculator", "../"]
]

def test(test_cases):
    for case in test_cases:
        if case[1] == '.':
            dir_word = 'current'
        else:
            dir_word = case[1]

        result = get_files_info(*case)

        print(f"Result for {dir_word} directory:")
        if result.startswith("Error"):
            print(f"  {result}")
        else:
            # Add two spaces to the start, then indent every subsequent line
            indented_result = "  " + result.replace("\n", "\n  ")
            print(indented_result)

if __name__ == "__main__":
    test(test_cases)



