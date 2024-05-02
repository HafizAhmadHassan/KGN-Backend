import multiprocessing
import subprocess
import threading
import sys

x = 0

def myfunc():
  global x
  x +=1
def run_script(arguments):
    subprocess.run(["python3", "csv_change.py"] + arguments)

if __name__ == "__main__":
    # List of arguments for the script

    # Initialize the script arguments list
    script_arguments = []

    # Define the number of argument sets per pattern
    sets_per_pattern = 1

    # Define the number of patterns
    num_patterns =10

    # Loop through each pattern
    for pattern_index in range(num_patterns):
        # Calculate the starting index for this pattern
        start_index = pattern_index * sets_per_pattern * 10 + 1
        
        # Generate argument sets for this pattern
        for i in range(sets_per_pattern):
            # Generate argument sets from 1 to 9 for each pattern
            for j in range(1, 10):
                script_arguments.append([str(int(sys.argv[1]) + start_index + i * 10 + j), str(j)])

    # Now script_arguments contains the desired 200 argument sets
    print(len(script_arguments))

    # Maximum number of threads to run concurrently
    max_threads = len(script_arguments)

    # Initialize variables to track running threads
    running_threads = []

    for arguments in script_arguments:
        # Start a new thread
        thread = threading.Thread(target=run_script, args=(arguments,))
        running_threads.append(thread)
        thread.start()
        myfunc()
        print("Thread start ", x)

        # Check if the maximum number of threads has been reached
        if len(running_threads) >= max_threads:
            # Wait for all running threads to complete before starting new ones
            for thread in running_threads:
                thread.join()
            running_threads = []

    # Wait for any remaining threads to complete
    for thread in running_threads:
        thread.join()



"""
# Create a process pool
    with multiprocessing.Pool() as pool:
        # Run the script with different arguments in parallel
        pool.map(run_script, script_arguments)
# Create threads for each set of arguments

"""
