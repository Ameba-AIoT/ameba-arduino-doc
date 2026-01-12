.. tags:: reparameterization, yolov7, amb82-mini

How to do reparameterization for customized YOLOv7-tiny model?
==============================================================

Reparameterization is used to reduce trainable BoF modules into deploy model for fast inference. For example merge BN to conv, merge YOLOR to conv, ..etc However, before reparameterization, the model has more parameters and computation cost.reparameterized model (cfg/deploy) used for deployment purpose

**Answer**

You may clone a copy of `YOLOv7 repo <https://github.com/WongKinYiu/yolov7>`__ into your local machine and perform reparameterization there.
Else, you may create a copy of this `Kaggle notebook <https://www.kaggle.com/code/kevinl00/yolov7-reparameterization-only>`__ upload your best trained model pt file and perform reparameterization on Kaggle. After running all the lines correctly, you can download your reparameterized model ``best_reparam.pt`` and use it on Ameba.
