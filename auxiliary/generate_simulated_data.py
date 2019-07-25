import respy as rp
import sys
import pandas as pd
import os

if __name__ == '__main__':
    if not os.path.exists('simulated_data'):
        os.mkdir('simulated_data')
    model_name = sys.argv[1]

    params, options, _ = rp.get_example_model(model_name)
    options['solution_draws'] = 250
    options['simulation_agents'] = 750
    state_space, data = rp.simulate(params, options)
    pd.to_pickle(data, os.path.join("simulated_data", f"{model_name}.pickle"))
