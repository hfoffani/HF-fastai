import typer
import os

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
    corpus = []
    
    idx = 0
    for d in os.listdir(corpusroot):
        if d.startswith('.'):
            continue
        for dg in os.listdir(corpusroot+"/"+d):
            if dg.endswith('-plain.txt'):
                cl = dg[0]
                with open(corpusroot+"/"+d+"/"+dg) as f:
                    lines = f.readlines()
                    for l in lines:
                        l = l.strip()
                        if len(l) > 1:
                            corpus.append( { 'idx':idx, 'label':keys[cl], 'sentence':l } )
                            idx += 1
    # print( len(corpus) )
    # print( corpus[0] )
    # print( corpus[-1])
    return corpus

if __name__ == "__main__":
    app()
