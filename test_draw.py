from uxsim import *


# Simulation main
W = World(
    name="simple_demo",
    deltan=5,
    tmax=7200,
    print_mode=1, save_mode=1, show_mode=0,
    random_seed=0
)

# Scenario definition
#load CSV files
W.load_scenario_from_csv("matsim/nodes_simplified.csv", "dat/siouxfalls_links.csv", "dat/siouxfalls_demand.csv")

# Simulation execution
W.exec_simulation()

# Results analysis
W.analyzer.print_simple_stats()

W.analyzer.network_anim(animation_speed_inverse=15, detailed=0, network_font_size=0)
W.analyzer.network_fancy(animation_speed_inverse=15, sample_ratio=0.1, interval=10, trace_length=5, speed_coef=4)