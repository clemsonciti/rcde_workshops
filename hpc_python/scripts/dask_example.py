from dask.distributed import Client
import dask.array as da

# Connect to the Dask scheduler
client = Client(scheduler_file='scheduler.json')

# Example: Creating a random Dask array and performing a computation
x = da.random.random((10000, 10000), chunks=(1000, 1000))
result = x.mean().compute()

print("Mean of the array:", result)

