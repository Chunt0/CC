
file_path = "/home/chunt/VScode/Python/CC/BirdData/kba_data.csv"

with open(file_path) as f:
    file = f.readlines()

for line in file:
    line = line.replace('\n', '')
    line = line.split(',')
    
    print(line)
    break