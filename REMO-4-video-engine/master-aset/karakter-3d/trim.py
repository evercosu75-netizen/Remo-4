from PIL import Image
import pathlib
here=pathlib.Path(__file__).parent.resolve()
raw=here/"renders"/"raw"; out=here/"renders"
for p in sorted(raw.glob("*.png")):
    im=Image.open(p).convert("RGBA")
    bbox=im.getbbox()
    print(p.name, "bbox", bbox, "size", im.size)
    if bbox:
        pad=12
        x0=max(0,bbox[0]-pad); y0=max(0,bbox[1]-pad)
        x1=min(im.width,bbox[2]+pad); y1=min(im.height,bbox[3]+pad)
        im.crop((x0,y0,x1,y1)).save(out/f"{p.stem}.png")
    else:
        print("  WARNING fully transparent", p.name)
