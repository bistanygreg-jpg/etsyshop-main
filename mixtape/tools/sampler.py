import soundfile as sf,numpy as np,subprocess,os
from kokoro_onnx import Kokoro
from PIL import Image,ImageDraw,ImageFont,ImageFilter
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
V=[("af_heart","Warm & friendly (current)","US woman",1.05,"en-us"),
   ("af_bella","Bright & upbeat","US woman",1.0,"en-us"),
   ("af_nicole","Soft, almost whispered","US woman",0.95,"en-us"),
   ("af_sarah","Calm storyteller","US woman",1.0,"en-us"),
   ("am_michael","Warm & steady","US man",1.05,"en-us"),
   ("am_fenrir","Deep & cinematic","US man",1.0,"en-us"),
   ("am_puck","Playful & young","US man",1.05,"en-us"),
   ("am_echo","Laid-back","US man",1.0,"en-us"),
   ("bf_emma","Gentle","British woman",1.0,"en-gb"),
   ("bm_george","Classic narrator","British man",1.0,"en-gb")]
lines=["Remember nineteen ninety-six?","Couples skate.","And nobody slept.","Mixtape Mercantile. Take me back."]
bg=Image.open("../canvadl/p1.jpg").convert("RGB").filter(ImageFilter.GaussianBlur(6))
bg=Image.eval(bg,lambda x:int(x*.45))
def font(n,s):
    for p in [f"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(p): return ImageFont.truetype(p,s)
    return ImageFont.load_default()
os.makedirs("smp",exist_ok=True); parts=[]
for i,(v,desc,who,sp,lang) in enumerate(V,1):
    sr=24000; seg=[np.zeros(int(sr*.35))]
    for l in lines:
        a,sr=k.create(l,voice=v,speed=sp,lang=lang); seg+=[a,np.zeros(int(sr*.18))]
    seg.append(np.zeros(int(sr*.5))); a=np.concatenate(seg); a=a/np.abs(a).max()*.9
    sf.write(f"smp/{i:02d}.wav",a,sr)
    im=bg.copy(); d=ImageDraw.Draw(im)
    d.text((540,700),f"VOICE {i}",font=font(0,150),fill=(255,201,60),anchor="mm")
    d.text((540,880),desc,font=font(0,70),fill="white",anchor="mm")
    d.text((540,980),who,font=font(0,54),fill=(46,230,214),anchor="mm")
    im.save(f"smp/{i:02d}.png")
    subprocess.run(["ffmpeg","-loglevel","error","-y","-loop","1","-i",f"smp/{i:02d}.png","-i",f"smp/{i:02d}.wav","-c:v","libx264","-tune","stillimage","-pix_fmt","yuv420p","-r","30","-c:a","aac","-b:a","160k","-shortest",f"smp/{i:02d}.mp4"])
    parts.append(f"file '{i:02d}.mp4'"); print(i,v,round(len(a)/sr,1),"s")
open("smp/list.txt","w").write("\n".join(parts))
subprocess.run(["ffmpeg","-loglevel","error","-y","-f","concat","-safe","0","-i","smp/list.txt","-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac","-af","loudnorm=I=-14:TP=-1.5","voice-sampler.mp4"])
