import sys
from Shapes3D import Shape3D, Cube, Cuboid, Cylinder, Sphere, 

def solve():
    total = 0
    shape_list = []

    if len(sys.argv) < 2:
        print("What is the name of the file in your terminal")
        return
    filename = sys.argv[1]

    with open(filename) as file:
        for line in file:
            line_data = line.strip().split(',')

            my_shape = None
            if line_data[0] == "cuboid":
                my_shape = Cuboid(
                    float(line_data[1]),
                    float(line_data[2]),
                    float(line_data[3])
                )
            elif line_data[0] == "cube":
                my_shape = Cube(
                    float(line_data[1])
                )
            elif line_data[0] == "cylinder":
                my_shape = Cylinder(
                    float(line_data[1]),
                    float(line_data[2])
                )
            elif line_data[0] == "sphere":
                my_shape = Sphere(
                    float(line_data[1])
                )
            elif line_data[0] == "area":
                for shape in shape_list:
                    total += shape.GetSurfaceArea() * float(line_data[1])
                shape_list.clear()
                continue
            elif line_data[0] == "volume":
                for shape in shape_list:
                    total += shape.GetVolume() * float(line_data[1])
                shape_list.clear()
                continue
            else:
                raise ValueError(f"Unable to parse shape from name '{line_data[0]}'")

            shape_list.append(my_shape)

    print(f"The sum of the measurements are {total:.2f}")

if __name__ == "__main__":
    solve()
