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

# Statically Determinate beam (Ex 12.14 Hibbeler)
# Determine the displacement at x = 8m for the following structure
# 8 m long fixed at A (x = 0m)
# A trapezoidal load of - 4000 N/m at x = 0 m descending to 0 N/m at x = 6 m.


# DEFINE BEAM
beam = Beam(8, E=1, I=1)  ##EI Defined to be 1 get the deflection as a function of EI

# DEFINE SUPPORTS HERE VIA SUPPORT CLASS
supports = [Support(0, (1, 1, 1)), Support(1, (1, 1, 0))]

# DEFINE LOADS HERE VIA LOAD CLASSES
loads = [TrapezoidalLoadV((-4000, 0), (0, 6))]

# ADD DEFINED SUPPORTS
beam.add_supports(*supports)

# ADD DEFINED LOADS
beam.add_loads(*loads)

beam.analyse()
print(f"Deflection is {beam.get_deflection(8)} N.m3 / EI (N.mm2)")

# EXPORT RESULTS INTO HTML

fig = beam.plot_beam_internal()
fig.write_html("./generated/determinate/internal.html")

fig2 = beam.plot_beam_external()
fig2.write_html("./generated/determinate/external.html")

fig3 = beam.plot_beam_diagram()
fig3.write_html("./generated/determinate/diagram.html")
print("=======================================================")
print("Results successfully exported at /generated/determinate")


# Note: all plots are correct, deflection graph shape is correct but for actual deflection values will need real EI properties.

##save the results as a pdf (optional)
# Can save figure using `fig.write_image("./results.pdf")` (can change extension to be
# html, jpg, svg or other formats as reired). Requires pip install -U kaleido
