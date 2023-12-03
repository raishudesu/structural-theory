# Arbritrary example defined in README.md
from indeterminatebeam import Beam, Support, PointLoadV, DistributedLoadV, PointTorque

beam = Beam(7)  # Initialize a Beam object of length 7 m with E and I as defaults
beam_2 = Beam(9, E=2000, I=100000)  # Initialize a Beam specifying some beam parameters

a = Support(5, (1, 1, 0))  # Defines a pin support at location x = 5 m
b = Support(0, (0, 1, 0))  # Defines a roller support at location x = 0 m
c = Support(7, (1, 1, 1))  # Defines a fixed support at location x = 7 m
beam.add_supports(a, b, c)

load_1 = PointLoadV(
    1000, 2
)  # Defines a point load of 1000 N acting up, at location x = 2 m
load_2 = DistributedLoadV(
    2000, (1, 4)
)  # Defines a 2000 N/m UDL from location x = 1 m to x = 4 m
load_3 = PointTorque(
    2 * 10**3, 3.5
)  # Defines a 2*10**3 N.m point torque at location x = 3.5 m
beam.add_loads(
    load_1, load_2, load_3
)  # Assign the support objects to a beam object created earlier

beam.analyse()

fig_1 = beam.plot_beam_external()
# fig_1.show() # this is not working for some reason

fig_2 = beam.plot_beam_internal()
# fig_2.show() # this is not working for some reason

# save the results (optional)
# Can save figure using ``fig.write_html("./results.pdf")`` (can change extension to be
# png, jpg, svg or other formats as reired). Requires pip install -U kaleido

fig_1.write_html("./generated/basic_usage_external.html")
fig_2.write_html("./generated/basic_usage_internal.html")
