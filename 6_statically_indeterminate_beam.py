from indeterminatebeam import (
    Beam,
    Support,
    PointTorque,
    PointLoad,
    PointLoadV,
    PointLoadH,
    UDL,
    UDLV,
    UDLH,
    TrapezoidalLoad,
    TrapezoidalLoadV,
    TrapezoidalLoadH,
    DistributedLoad,
    DistributedLoadV,
    DistributedLoadH,
)

# Note: load ending in V are vertical loads
# load ending in H are horizontal loads
# load not ending in either takes angle as an input (except torque)

# Statically Indeterminate beam (Ex 12.21 Hibbeler)
# Determine the reactions at the roller support B of the beam described below:
# 3 m long, fixed at A (x = 0 m), roller support at B (x=3 m),
# vertical point load at midpan of 8000 N, UDL of 6000 N/m, EI constant.

# DEFINE BEAM
beam = Beam(3)

# DEFINE SUPPORTS VIA SUPPORT CLASS
supports = [Support(0, (1, 1, 1)), Support(3, (0, 1, 0))]

# DEFINE LOADS VIA LOAD CLASSES
loads = [PointLoadV(-8000, 1.5), UDLV(-6000, (0, 3))]

# INITIALIZE ADDED SUPPORTS
beam.add_supports(*supports)

# INITIALIZE ADDED LOADS
beam.add_loads(*loads)

beam.analyse()

# RESULTS
print(
    f"The beam has an absolute maximum shear force of: {beam.get_shear_force(return_absmax=True)} N"
)
print(
    f"The beam has an absolute maximum bending moment of: {beam.get_bending_moment(return_absmax=True)} N.mm"
)
print(f"The beam has a vertical reaction at B of: {beam.get_reaction(3,'y')} N")

fig1 = beam.plot_beam_external()

fig2 = beam.plot_beam_internal()
fig3 = beam.plot_beam_diagram()

fig1.update_layout(width=600)
fig2.update_layout(width=600)

# EXPORT RESULTS

fig1.write_html("./generated/indeterminate/external.html")
fig2.write_html("./generated/indeterminate/internal.html")
fig3.write_html("./generated/indeterminate/diagram.html")

print("=======================================================")
print("Results successfully exported at /generated/indeterminate")
