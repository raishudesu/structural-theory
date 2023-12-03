from indeterminatebeam import (
    Beam,
    Support,
    PointTorque,
    PointLoad,
    PointLoadH,
    PointLoadV,
    UDL,
    UDLH,
    UDLV,
    TrapezoidalLoad,
    TrapezoidalLoadH,
    TrapezoidalLoadV,
    DistributedLoad,
    DistributedLoadH,
    DistributedLoadV,
)


# Function to create supports based on specified degree of freedom combinations
def create_support_by_type(support_type, coord):
    if support_type == 0:
        print(
            f"Support at x-coordinate {coord} meters: Degrees of freedom: (1, 1, 1) - Conventional fixed support"
        )
        return Support(coord, (1, 1, 1))  # conventional fixed support
    elif support_type == 1:
        print(
            f"Support at x-coordinate {coord} meters: Degrees of freedom: (1, 1, 0) - Conventional pin support"
        )
        return Support(coord, (1, 1, 0))  # conventional pin support
    elif support_type == 2:
        print(f"Support at x-coordinate {coord} meters: Degrees of freedom: (1, 0, 1)")
        return Support(coord, (1, 0, 1))
    elif support_type == 3:
        print(f"Support at x-coordinate {coord} meters: Degrees of freedom: (0, 1, 1)")
        return Support(coord, (0, 1, 1))
    elif support_type == 4:
        print(f"Support at x-coordinate {coord} meters: Degrees of freedom: (0, 0, 1)")
        return Support(coord, (0, 0, 1))
    elif support_type == 5:
        print(
            f"Support at x-coordinate {coord} meters: Degrees of freedom: (0, 1, 0) - Conventional roller support"
        )
        return Support(coord, (0, 1, 0))  # conventional roller support
    elif support_type == 6:
        print(f"Support at x-coordinate {coord} meters: Degrees of freedom: (1, 0, 0)")
        return Support(coord, (1, 0, 0))
    else:
        print("Invalid support type. Using default: Free support.")
        return Support(coord, (0, 0, 0))  # Default: Free support


def create_load_by_type(load_type):
    if load_type == 0:
        force = float(input("Enter force: "))
        coord = float(input("Enter coord: "))
        return PointTorque(force=force, coord=coord)
    elif load_type == 1:
        force = float(input("Enter force: "))
        coord = float(input("Enter coord: "))
        angle = float(input("Enter angle: "))
        return PointLoad(force=force, coord=coord, angle=angle)
    elif load_type == 2:
        force = float(input("Enter force: "))
        coord = float(input("Enter coord: "))
        return PointLoadH(force=force, coord=coord)
    elif load_type == 3:
        force = float(input("Enter force: "))
        coord = float(input("Enter coord: "))
        angle = float(input("Enter angle: "))
        return PointLoadV(force=force, coord=coord, angle=angle)
    elif load_type == 4:
        force = float(input("Enter force: "))
        span_x = float(input("Enter span x: "))
        span_y = float(input("Enter span y: "))
        angle = float(input("Enter angle: "))
        return UDL(force=force, span=(span_x, span_y), angle=angle)
    elif load_type == 5:
        force_x = float(input("Enter force x: "))
        force_y = float(input("Enter force y: "))
        span_x = float(input("Enter span x: "))
        span_y = float(input("Enter span y: "))
        angle = float(input("Enter angle: "))
        return TrapezoidalLoad(
            force=(force_x, force_y), span=(span_x, span_y), angle=angle
        )
    elif load_type == 6:
        force_x = float(input("Enter force x: "))
        force_y = float(input("Enter force y: "))
        span_x = float(input("Enter span x: "))
        span_y = float(input("Enter span y: "))
        return TrapezoidalLoadV((force_x, force_y), (span_x, span_y))
    elif load_type == 7:
        expr = str(input("Enter expression: "))
        span_x = float(input("Enter span x: "))
        span_y = float(input("Enter span y: "))
        angle = float(input("Enter angle: "))
        return DistributedLoad(expr=expr, span=(span_x, span_y), angle=angle)


beamLength = float(input("Enter beam length in meters: "))
beam_e = float(input("Enter E: "))
beam_i = float(input("Enter I: "))

# Get the number of supports from the user
num_supports = int(input("Enter the number of supports to add: "))
supports = []

num_loads = int(input("Enter the number of loads to add: "))
loads = []

# Create supports based on user input for type
for i in range(num_supports):
    coord = float(input(f"Enter x-coordinate of support {i+1} on beam in meters: "))
    print("Choose support type (0 - 6): ")
    print("0 - Conventional fixed support (1, 1, 1)")
    print("1 - Conventional pin support (1, 1, 0)")
    print("2 - Degrees of freedom: (1, 0, 1)")
    print("3 - Degrees of freedom: (0, 1, 1)")
    print("4 - Degrees of freedom: (0, 0, 1)")
    print("5 - Conventional roller support (0, 1, 0)")
    print("6 - Degrees of freedom: (1, 0, 0)")
    support_type = int(input("Enter the type of support (0/1/2/3/4/5/6): "))
    support = create_support_by_type(support_type, coord)
    supports.append(support)

for i in range(num_loads):
    print("Choose load type (0 - 6): ")
    print("0 - Point Torque")
    print("1 - Point Load")
    print("2 - Point Load Horizontal")
    print("3 - Point Load Vertical")
    print("4 - UDL")
    print("5 - Trapezoidal Load")
    print("6 - Trapezoidal Load Vertical")
    print("7 - Distributed Load")
    load_type = int(input("Enter the type of load (0/1/2/3/4/5/6): "))
    load = create_load_by_type(load_type)
    loads.append(load)

beam = Beam(beamLength, E=beam_e, I=beam_i)
beam.add_supports(*supports)
beam.add_loads(*loads)

beam.analyse()
print(f"Deflection is {beam.get_deflection(beamLength)} N.m3 / EI (N.mm2)")

fig_diagram = beam.plot_beam_diagram()
fig_diagram.write_html("./determinate_diagram.html")

fig_internal = beam.plot_beam_internal()
fig_internal.write_html("./determinate_internal.html")

fig_external = beam.plot_beam_external()
fig_external.write_html("./determinate_external.html")
