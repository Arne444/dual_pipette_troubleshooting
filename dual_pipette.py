## Code to test dual pipetting capabilities of opentrons

from opentrons import robot, containers, instruments

source_tubes = containers.load('tube-rack-2ml', 'D2', 'tube rack')
output = containers.load('96-PCR-flat', 'C1', 'output')

p200rack = containers.load('tiprack-10ul-H', 'A1', 'p200-rack')
		
p200 = instruments.Pipette(
    tip_racks=[p200rack],
    min_volume=20,
    max_volume=200,
    axis="b"
)

for i in range(5):
	p200.pick_up_tip()
	p200.return_tip()