from functions.get_file_content import get_file_content

LIMIT = 10000 
TRUNCATE_MSG = "truncated at"

test_cases = [
    ("calculator", "lorem.txt"),
]
def main(test_cases):
    for wd, path in test_cases:
        content = get_file_content(wd, path)
        
        print(f"--- Testing: {path} ---")

        # Check 1: does it return an error string
        if content.startswith("Error:"):
            if content.startswith("Error: An unexpected error occurred:"):
                print(f"Un expected error in test {content}")
            print(f"Error detected {content}")
            continue
        
        # Check 1: Is it truncated?
        is_truncated = TRUNCATE_MSG in content
        print(f"Truncation detected: {is_truncated}")
        
        # Check 2: Content length logic
        # If truncated, the 'raw' content part should be exactly LIMIT
        if is_truncated:
            # We find where your message starts to check the length before it
            actual_data_length = content.find(f'[...File') 
            print(f"Data length before message: {actual_data_length}")
        else:
            print(f"Full file length: {len(content)}")
        print("\n")

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main(test_cases)