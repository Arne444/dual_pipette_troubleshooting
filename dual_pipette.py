## Code to test dual pipetting capabilities of opentrons

from opentrons import robot, containers, instruments

source_tubes = containers.load('tube-rack-2ml', 'D2', 'tube rack')
output = containers.load('96-PCR-flat', 'C1', 'output')

p200rack = containers.load('tiprack-10ul-H', 'A1', 'p200-rack')
trash = containers.load('trash-box', 'A3')

p200 = instruments.Pipette(
    trash_container=trash,
    tip_racks=[p200rack],
    min_volume=20,
    max_volume=200,
    axis="b"
)

p200.start_at_tip(p20rack['H1'])

p200.distribute(
	50
	source_tubes.wells('A1')
	output.wells('A1' to='D1')
	new_tip='always'
)
