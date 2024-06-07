import csv
import codecs
import sys
import os

def read_subcaps(input_file, output_csv):
    csv_rows = []
    with codecs.open(input_file, 'r', encoding='utf-16-le') as file:
        content = file.read()
        lines = content.replace('\r', '').split('\n')[3:-2]
        sanitized_lines = [item for item in lines if item != '']

        linecount = 0
        start = ''
        end = ''

        for line in sanitized_lines:
            linecount += 1
            # print(line)

            if (linecount % 2) == 0:
                shotcode=True
                csv_row = (line, start, end)
                csv_rows.append(csv_row)
            else:
                shotcode=False
                start, end = line.split()

        with open(output_csv, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(['Shot Code', 'Start Timecode', 'End Timecode'])
            writer.writerows(csv_rows)
        print(f"CSV file '{output_csv}' created successfully!")


if __name__ == '__main__':
    if len(sys.argv)>=2:
        input_file_path = str(sys.argv[1])#try to pass first argument as the file path
    else:
        input_file_path = input("Enter the path to the subcap txt file")
    if os.path.exists(input_file_path) and input_file_path.endswith('.txt'):
            read_subcaps(input_file_path, input_file_path.replace('.txt','.csv'))
