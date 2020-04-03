from dask.distributed import Client, LocalCluster
from multiprocessing import cpu_count
from typing import Tuple


def init_worker():
    import notebooks_as_modules


def setup_dask_cluster(num_workers: int = 0, threads_per_worker: int = 1) -> Tuple[Client, LocalCluster]:
    cluster = LocalCluster(n_workers=(num_workers or cpu_count()), threads_per_worker=threads_per_worker)
    client = Client(cluster)
    client.run(init_worker)
    return client, cluster