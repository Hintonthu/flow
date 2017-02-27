import logging

from cistar.core.exp import SumoExperiment
from cistar.envs.loop_accel import SimpleAccelerationEnvironment
from cistar.scenarios.loop.loop_scenario import LoopScenario
from cistar.controllers.car_following_models import *
from cistar.controllers.lane_change_controllers import *

logging.basicConfig(level=logging.INFO)

sumo_params = {"port": 8873, "time_step":0.01}

sumo_binary = "sumo-gui"

type_params = {"cfm_slow": (22, make_better_cfm(v_des=8), never_change_lanes_controller())}

env_params = {"target_velocity": 25}

net_params = {"length": 230, "lanes": 1, "speed_limit":35, "resolution": 40, "net_path":"dan-work/net/"}

cfg_params = {"start_time": 0, "end_time":50000, "cfg_path":"dan-work/cfg/"}

initial_config = {"shuffle":False}

scenario = LoopScenario("test-exp", type_params, net_params, cfg_params, initial_config)
##data path needs to be relative to cfg location
leah_sumo_params = {"port": 8873}

exp = SumoExperiment(SimpleAccelerationEnvironment, env_params, sumo_binary, sumo_params, scenario)

logging.info("Experiment Set Up complete")

exp.run(400, 1000)

exp.env.terminate()
