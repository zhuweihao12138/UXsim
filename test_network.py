from uxsim import *

W = World(
    name="sioufalls_matsim_network",    # Scenario name. Can be blank. Used as the folder name for saving results.
    deltan=1,   # Simulation aggregation unit Δn. Defines how many vehicles are grouped together (i.e., platoon size) for computation. Computation cost is generally inversely proportional to deltan^2.
    tmax=10500,  # Total simulation time (s)
    print_mode=1, save_mode=1, show_mode=1,    # Various options. print_mode determines whether to print information. Usually set to 1, but recommended 0 when running multiple simulations automatically. save_mode determines if visualization results are saved. show_mode determines if visualization results are displayed. It's good to set show_mode=1 on Jupyter Notebook, otherwise recommended 0.
    random_seed=0    # Set the random seed. Specify if you want repeatable experiments. If not, set to None.
)

W.generate_Nodes_from_csv("matsim/nodes_and_facilities.csv")
W.generate_Links_from_csv("matsim/links.csv")

W.show_network(figsize=(16,16),network_font_size=0,node_size=0.5)