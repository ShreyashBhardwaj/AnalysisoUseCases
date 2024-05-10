import asyncio
import concurrent.futures
import time
import matplotlib.pyplot as plt

# Define the data processing task
def process_data(num):
    return num * num

# Asynchronous data processing
async def process_data_asynchronously(data):
    start_time = time.time()
    results = await asyncio.gather(*[process_data(num) for num in data])
    return time.time() - start_time

# Parallel data processing
def process_data_in_parallel(data):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_data, data))
    return time.time() - start_time

# Main function
async def main():
    # Generate some sample data
    data = list(range(1, 1001))

    # Perform asynchronous data processing
    async_time = await process_data_asynchronously(data)

    # Perform parallel data processing
    parallel_time = process_data_in_parallel(data)

    return async_time, parallel_time

# Run the main coroutine and plot the results
async def run():
    async_time, parallel_time = await main()

    plt.bar(['Asynchronous', 'Parallel'], [async_time, parallel_time], color=['blue', 'orange'])
    plt.xlabel('Programming Paradigm')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Asynchronous vs Parallel Data Processing')
    plt.show()

await run()
