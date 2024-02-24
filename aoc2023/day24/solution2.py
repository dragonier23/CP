import sympy

filename = 'problemstatement.txt' # 'test.txt' # 
file = open(filename, 'r').readlines()

paths = [list(map(int, line.strip().replace(" @ ", ", ").split(", "))) for line in file]\

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for sx, sy, sz, vx, vy, vz in paths:
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

ans = sympy.solve(equations)[0]
print(ans)
print(ans[xr] + ans[yr] + ans[zr])