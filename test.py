from uxsim import *
import csv
# Define the main simulation
# Units are standardized to seconds (s) and meters (m)
# Simulation main

# The earliest time in end_time1 is: 06:24:48
W = World(
    name="test",
    deltan=1,
    tmax=10500,
    print_mode=1, save_mode=1, show_mode=1,
    random_seed=0
)

W.generate_Nodes_from_csv("dat/siouxfalls_nodes.csv")
W.generate_Links_from_csv("dat/siouxfalls_links.csv")

W.show_network()