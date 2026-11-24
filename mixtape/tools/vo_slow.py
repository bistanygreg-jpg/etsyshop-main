import soundfile as sf,numpy as np,json
from kokoro_onnx import Kokoro
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
lines=["Remember nineteen ninety-six?","Rewinding every tape.","Stretching the phone cord.","Waiting forever for one picture.","Couples skate.","And nobody slept."]
end_lines=["Mixtape Mercantile.","Take me back."]
sr=24000; clips=[]; t=0.5; starts=[]
for l in lines:
    a,sr=k.create(l,voice="af_nicole",speed=1.0,lang="en-us")
    starts.append(t); clips.append((t,a)); t+=len(a)/sr+0.85   # pause after each line
end_start=t-0.35                       # end card appears
t=end_start+0.9
for l in end_lines:
    a,sr=k.create(l,voice="af_nicole",speed=0.92,lang="en-us"); clips.append((t,a)); t+=len(a)/sr+0.55
total=round(t+1.3,1)
out=np.zeros(int(sr*total))
for s,a in clips: i=int(s*sr); out[i:i+len(a)]+=a
for d,g in((0.045,.2),(0.09,.11),(0.14,.05)):
    m=int(d*sr); out[m:]+=g*out[:-m]
sf.write("vo_slow.wav",out/np.abs(out).max()*.9,sr)
json.dump({"starts":starts,"end":end_start,"total":total},open("slow.json","w"))
print([round(s,2) for s in starts],round(end_start,2),total)
