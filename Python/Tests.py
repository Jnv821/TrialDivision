import math
import time
import TrialDivision as td


### Functions that will be tested


### Run functions and return their execution time
        
def run_function(outputFile):
    result_times = []
    primes = {1,2,3,5}
    for i in range(1, 7):  # Loop to 1 Billion
        start_time = time.perf_counter_ns()
        for j in range(10 ** i):  # Nested loop with iterations increasing by 10 times each time
            td.trial_division_5(j)
        end_time = time.perf_counter_ns()
        result_time = (end_time-start_time)/10**9
        result_times.append(result_time)
        result = f"Result time for 10^{i}: {result_time:.9f} seconds"
        write_to_file(outputFile, result)
    return result_times

def average_times(lists):
    num_lists = len(lists)
    num_times = min(len(lst) for lst in lists) # Assuming all lists have the same length
    
    averaged_times = []
    
    for i in range(num_times):
        total = sum(lst[i] for lst in lists)
        average = total / num_lists
        averaged_times.append(average)
    
    return averaged_times

### File management


        
def createFile(filename):
    open(filename, "w").close()

def write_to_file(filename,string):
    with open("./"+filename, "a") as file:
        file.write(string)
        file.write("\n")
        file.close()

def test(filename, number_of_runs):
    run_times = []
    for n in range(1, number_of_runs+1):
        write_to_file(filename, f"==== Test Number: {n} ====")
        run_times.append(run_function(filename))
        write_to_file(filename, f"==========================\n")
    write_to_file(filename, "==== Averages ====")
    averaged_times = average_times(run_times)
    for m in range(0, len(averaged_times)):
        write_to_file(filename, f"Average for 10^{m+1} ran {number_of_runs} times: {averaged_times[m]:.9f} seconds")

def p (t):
    print({t})  
### Main 
if __name__ == "__main__":
    filename = "./results_6.txt"
    createFile(filename)
    #number = int(input("Introduzca el número a revisar: "))
    test(filename,5)

