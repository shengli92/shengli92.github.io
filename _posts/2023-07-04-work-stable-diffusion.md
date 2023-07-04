---
layout: post
tags: [stable diffusion]
---

{% include JB/setup %}


启动stable diffusion报错
```shell
RuntimeError: MPS backend out of memory (MPS allocated: 5.05 GB, other allocations: 1.29 GB, max allowed: 6.77 GB).
```

启动命令改成
```shell
PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.7 ./webui.sh --precision full --no-half
```
即可解决