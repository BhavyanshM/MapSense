from pydrake.common import FindResourceOrThrow
from pydrake.multibody.parsing import Parser
from pydrake.multibody.plant import AddMultibodyPlantSceneGraph
from pydrake.systems.analysis import Simulator
from pydrake.systems.framework import DiagramBuilder

builder = DiagramBuilder()
plant, _ = AddMultibodyPlantSceneGraph(builder, 0.0)

sdf = '/home/bmishra/Workspace/Code/repository-group/nadia/nadia-hardware-drivers/src/main/resources/models/nadia_V16_description/sdf/nadiaV16.tmotorGrippers.fullRobot.sdf'



Parser(plant).AddModelFromFile(sdf, file_type='sdf')

plant.Finalize()
diagram = builder.Build()


simulator = Simulator(diagram)