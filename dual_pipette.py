## Code to test dual pipetting capabilities of opentrons

from opentrons import robot, containers, instruments

source_tubes = containers.load('tube-rack-2ml', 'D2', 'tube rack')
output = containers.load('96-PCR-flat', 'C1', 'output')

p200rack = containers.load('tiprack-200ul', 'A1', 'p200-rack')
trash = containers.load('trash-box', 'A3')

p200 = instruments.Pipette(
    trash_container=trash,
    tip_racks=[p200rack.cols('A', 'B')],
    min_volume=20,
    max_volume=200,
    axis="b"
)

for i in range(10):
	p200.pick_up_tip()
	p200.return_tip()
