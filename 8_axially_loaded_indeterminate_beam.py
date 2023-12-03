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

##AXIAL LOADED INDETERMINATE BEAM (Ex 4.13 Hibbeler)
## A rod with constant EA has a force of 60kN applied at x = 0.1 m, and the beam has fixed supports at x=0, and x =0.4 m. Determine the reaction forces.

# DEFINE BEAM
beam = Beam(0.4)

# DEFINE SUPPORTS
supports = [Support(), Support(0.4)]

# DEFINE LOADS
loads = [PointLoadH(-60000, 0.1)]

# INITIALIZE DEFINED SUPPORTS
beam.add_supports(*supports)

# INITIALIZE DEFINED LOADS
beam.add_loads(*loads)

beam.analyse()
beam.plot_normal_force()

# EXPORT RESULTS
fig = beam.plot_beam_internal()
fig.write_html("./generated/axial/internal.html")

fig2 = beam.plot_beam_external()
fig2.write_html("./generated/axial/external.html")

fig3 = beam.plot_beam_diagram()
fig3.write_html("./generated/axial/diagram.html")
print("=======================================================")
print("Results successfully exported at /generated/axial")
