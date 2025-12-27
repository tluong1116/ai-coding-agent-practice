from functions.write_file import write_file
test_cases = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

def test(test_cases):
    for case in test_cases:
        print(write_file(*case))

if __name__ == '__main__':
    test(test_cases)