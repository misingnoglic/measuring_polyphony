# For now this is where I am just putting a scratch pad for my progress

import verovio
tk = verovio.toolkit(False)

tk.setResourcePath(r"C:\Users\misin\OneDrive\Documents\GitHub\verovio\data")
tk.setNoLayout(True)
tk.setFormat("mei")
tk.loadFile("vos_pastores_MENSURAL.mei")
tk.renderToSvgFile("test.svg", 1)