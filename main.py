from app.io import input
from app.io import output


def main():
    text_input_result = input.text_input()
    file_input_result = input.read_from_file('data\\something.txt')
    pandas_input_result = input.read_with_pandas('data\\addresses.csv')

    output.output_to_console(f'Old text from `something.txt`: {file_input_result}')
    output.output_to_console(f'You typed: {text_input_result}. This text will be written to `something.txt`')
    print("addresses.csv: ")
    output.output_to_console(pandas_input_result.to_string())
    output.write_to_file(text_input_result, 'data\\something.txt')


if __name__ == '__main__':
    main()
