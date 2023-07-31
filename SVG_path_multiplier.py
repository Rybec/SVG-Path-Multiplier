
import sys
import xml.dom.minidom

if len(sys.argv) != 3:
	print("Usage: python SVG_path_multiplier.py <filename> <pass count>")
	print()
	print("\tOutput file will be saved as the original filename")
	print("\tprepended with 'x-passes_', where x is the number of")
	print("\tpasses specified.")
	print()
	print("\tThis program duplicates each path the specified number")
	print("\tof times, group duplicate paths together.  When used for")
	print("\tlaser cutting with programs like LaserGRBL, this will")
	print("\tcause each path to be cut in multiple subsequent passes,")
	print("\tbefore moving on to the next path.  In most instances,")
	print("\tthis will produce superior cutting results compared to")
	print("\tdoing the entire cut program in each pass before moving")
	print("\tto the next pass, because far less time will be allowed")
	print("\tto pass between passes, giving the media less time to")
	print("\tcool down and absorb moisture from the air (in case of")
	print("\tof wood) between passes.")
	print()
	sys.exit()


svg_file = sys.argv[1]
passes = int(sys.argv[2])

svg_dom = xml.dom.minidom.parse(svg_file)

paths = svg_dom.getElementsByTagName("path")


for path in paths:
	group = svg_dom.createElement("g")
	group.setAttribute("id", "g" + path.getAttribute("id"))

	for i in range(passes):
		new_path = path.cloneNode(True)
		new_path.setAttribute("id", new_path.getAttribute("id") + str(1000 + i))
		group.appendChild(new_path)

	path.parentNode.insertBefore(group, path)
	path.parentNode.removeChild(path)


with open("{}-pass_{}".format(passes, svg_file), "w") as outfile:
	svg_dom.writexml(outfile)


