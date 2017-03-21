# For now this is where I am just putting a scratch pad for my progress
# Github links from questions I've asked from verovio:
# https://github.com/rism-ch/verovio/issues/523
# https://github.com/rism-ch/verovio/issues/491
# https://github.com/rism-ch/verovio/issues/490


import verovio
tk = verovio.toolkit(False)

# The path for my resource folder - probably will change on server
tk.setResourcePath(r"C:\Users\misin\OneDrive\Documents\GitHub\verovio\data")

# Suggested by developer on github for mensural MEI files
tk.setNoLayout(True)

# Needed to tell the verovio that it is mei
tk.setFormat("mei")

# loads the mei file
tk.loadFile("vos_pastores_MENSURAL.mei")

# saves as SVG
tk.renderToSvgFile("test.svg", 1)