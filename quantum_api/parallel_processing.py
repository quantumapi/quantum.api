from multiprocessing import Pool

def parallel_simulate(circuits):
    with Pool(processes=4) as pool:
        results = pool.map(simulate_quantum_circuit, circuits)
    return results
