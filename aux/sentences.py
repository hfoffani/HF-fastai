import typer
import os
import glob

app = typer.Typer()

keys = {
        'a':'environment',
        'm':'medicine',
        'i':'technology',
        'e':'economy',
        'd':'legal',
}

@app.command()
def sentences(corpusroot: str):
    listfiles = glob.glob(corpusroot + '/*/*-plain.txt')
    corpus = []
    idx = 0
    for fname in listfiles:
        cl = os.path.basename(fname)[0]
        with open(fname) as f:
            for l in f.readlines():
                l = l.strip()
                if len(l) > 1:
                    corpus.append( {'idx':idx, 'label':keys[cl], 'sentence':l } )
                    idx += 1
    return corpus

if __name__ == "__main__":
    app()
