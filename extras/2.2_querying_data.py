# Arbritrary example defined in README.md
from indeterminatebeam import (
    Beam,
    Support,
    PointLoadV,
    PointTorque,
    UDLV,
    DistributedLoadV,
)

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

# fig_1.write_html("./diagram.html")
# fig_2.write_html("./internal.html")


# Run section 2a (prior to running this example)

# query for the data at a specfic point (note units are not provided)
print("bending moments at 3 m: " + str(beam.get_bending_moment(3)))
print("shear forces at 1,2,3,4,5m points: " + str(beam.get_shear_force(1, 2, 3, 4, 5)))
print("normal force absolute max: " + str(beam.get_normal_force(return_absmax=True)))
print("deflection max: " + str(beam.get_deflection(return_max=True)))

##add a query point to a plot (adds values on plot)
beam.add_query_points(1, 3, 5)
beam.remove_query_points(5)

## plot the results for the beam
fig = beam.plot_beam_internal()
fig.write_html("./generated/2querying_data.html")
# fig.show()
