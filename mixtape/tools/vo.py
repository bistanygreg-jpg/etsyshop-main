import sys,soundfile as sf,numpy as np
from kokoro_onnx import Kokoro
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
voice=sys.argv[1]; sp=float(sys.argv[2])
# (start seconds, line)
L=[(0.15,"Remember nineteen ninety-six?"),
   (1.55,"Rewinding every tape."),
   (3.05,"Stretching the phone cord."),
   (4.55,"Waiting forever for one picture."),
   (6.05,"Couples skate."),
   (7.55,"And nobody slept."),
   (9.2,"Mixtape Mercantile."),
   (10.3,"Take me back.")]
cur=0.0
sr=24000; out=np.zeros(int(sr*14),dtype=np.float32)
for t,line in L:
    a,sr=k.create(line,voice=voice,speed=sp,lang="en-us")
    t=max(t,cur+0.06); i=int(t*sr); n=min(len(a),len(out)-i); out[i:i+n]+=a[:n]; cur=t+len(a)/sr
    print(f"{t:5.2f}s -> {cur:5.2f}s  {line}")
out=out/max(1e-6,np.abs(out).max())*0.89
sf.write(f"vo_{voice}.wav",out,sr)
