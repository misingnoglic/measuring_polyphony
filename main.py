# For now this is where I am just putting a scratch pad for my progress
# Github links from questions I've asked from verovio:
# https://github.com/rism-ch/verovio/issues/523
# https://github.com/rism-ch/verovio/issues/491
# https://github.com/rism-ch/verovio/issues/490

from flask import Flask,render_template
import glob

app = Flask(__name__)

@app.route('/render_svg/<folder>/<name>')
def render_file(folder, name):
    return mei_to_svg(fr"mei_files\{folder}\{name}")

@app.route('/')
def home():
    s = "\\"
    meis = glob.glob(r"mei_files\*\*_MENSURAL.mei")
    meis = [ (mei, mei.split(s)[1:]) for mei in meis]
    #return str(meis)
    return render_template("index.html", meis=meis)

import verovio


def load_mei_tk(mensural=True):
    tk = verovio.toolkit(False)
    # The path for my resource folder - probably will change on server
    tk.setResourcePath(r"C:\Users\misin\OneDrive\Documents\GitHub\verovio\data")
    # Suggested by developer on github for mensural MEI files
    if mensural:
        tk.setNoLayout(True)
        #tk.setPageHeight(800)
        #tk.setPageWidth(2)
    tk.setFormat("mei")
    return tk



def mei_to_svg(file_path: str):
    tk = load_mei_tk()
    tk.loadFile(file_path)
    svg_string = tk.renderToSvg(1)
    return svg_string

if __name__ == "__main__":
    app.run()