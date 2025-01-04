def get_own_content():
    try:
        print(f"Attempting to read file: {__file__}")  # Debug
        with open(__file__, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"Content length: {len(content)}")  # Debug
        return content
    except Exception as e:
        print(f"Exception occurred: {str(e)}")  # Debug
        return f"Error reading file: {str(e)}"


def main():
    user_input = input("Enter 'src' to view the source code: ")
    if user_input.lower() == "src":
        return get_own_content()
    else:
        return "Input not recognized. Enter 'src' to view source code."


if __name__ == "__main__":
    result = main()
    print("---Output starts---")  # Debug
    print(result)
    print("---Output ends---")  # Debug
