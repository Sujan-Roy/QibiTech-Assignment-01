from concurrent.futures import ThreadPoolExecutor
import threading
import re
import glob
import os

readPath = "dataset/"
readPath2 = "dataset\\"
newPath="Extract_Data_directory/"

class AverageCalculator:
    def __init__(self, filename, num_threads):
        self.filename = filename
        self.num_threads = num_threads
        self.lock = threading.Lock()
        self.total_sum = 0
        self.total_count = 0
# calculate_average method uses a thread pool to process each line of the file in parallel, submitting each line to the _process_line method. 
    def calculate_average(self):
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            with open(self.filename, 'r') as f:
                for line in f:
                    executor.submit(self._process_line, line.strip())

    def _process_line(self, line):
        try:
            value = float(line)
        except ValueError:
            print(f"Skipping invalid input: {line}")
            return
        with self.lock:
            self.total_sum += value
            self.total_count += 1
# Calculte the average
    def get_average(self):
        with self.lock:
            if self.total_count == 0:
                return 0
            return self.total_sum / self.total_count
        
#Create new directory if the diserd directory is not exist
def create_dir(self):
    print('hello world')
if not os.path.exists(newPath):
    print('exists')
    os.makedirs(newPath)

# EXtarct only required data from the input text file and return the data using list
def input_text(files):
    dBm_list=[]
    with open(files, 'r') as file:
        for n in file:
            sp = n.split()
            for i in re.findall(r'\d+', sp[3]):
                dBm_list.append(int(i))
        return dBm_list



def main():
    # Access all the .txt file using golb function
    # pass the text 
    file_path = glob.glob(readPath+'*.txt')
    for item in file_path:
        x = item.replace(readPath2, "") # create the new .txt file name same as input .txt file.
        # Pass the all input .txt file in the defined input_text function
        inputText = input_text(item)
        # Pass the a filename and number of threads as inputs. 
        calculator = AverageCalculator(newPath+'saved_'+x, 4) 
        with open(newPath+'saved_'+x, 'w') as file:
            for data in inputText:
                file.write("%i\n" % data)
        # Calculte the average of the text file
        calculator.calculate_average()
        print(calculator.get_average())

if __name__ == "__main__":
    main()

