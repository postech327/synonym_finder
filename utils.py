def parse_table(text):
    lines = [line.strip() for line in text.strip().split('\n') if '|' in line]
    data = [line.split('|') for line in lines[1:]]  # skip header
    return [list(map(str.strip, row)) for row in data]
