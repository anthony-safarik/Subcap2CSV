import csv
import codecs

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
        # Process the content as needed


# Example usage
input_text_file = 'durations.txt'
output_csv_file = 'subtitles.csv'
# text_to_csv_from_file(input_text_file, output_csv_file)
read_subcaps(input_text_file, output_csv_file)
