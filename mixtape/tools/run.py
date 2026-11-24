import sys,cv2,numpy as np,onnxruntime as ort
s=ort.InferenceSession("depth/model.onnx",providers=["CPUExecutionProvider"])
inp=s.get_inputs()[0].name
for f in sys.argv[1:]:
    im=cv2.imread(f)[:,:,::-1].astype(np.float32)/255
    h,w=im.shape[:2]; H,W=518*2//14*14, 294  # keep 9:16-ish multiple of 14
    H,W=924,518
    x=cv2.resize(im,(W,H),interpolation=cv2.INTER_CUBIC)
    x=(x-[0.485,0.456,0.406])/[0.229,0.224,0.225]
    x=x.transpose(2,0,1)[None].astype(np.float32)
    d=s.run(None,{inp:x})[0][0]
    d=cv2.resize(d,(w,h),interpolation=cv2.INTER_CUBIC)
    d=(d-d.min())/(d.max()-d.min())   # 1 = near
    np.save(f.replace(".jpg","_depth.npy"),d)
    cv2.imwrite(f.replace(".jpg","_depth.png"),(d*255).astype(np.uint8))
    print(f,d.shape)
