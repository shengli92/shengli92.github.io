---
layout: post
title: "Remove untracked files from Git working tree"
description: ""
category: 
tags: []
---
{% include JB/setup %}

#### How to delete untracked local files from current working tree?


Step 1 is show what will be deleted by using the ```-n``` option:
```
  git clean -n
```

Clean Step -b beware:this will delete files:
```
git clean -f
```

+ To remove directories,run ```git clean -f -d``` or ```git clean -fd```
+ To remove ignored files, run ```git clean -f -X ``` or ```git clean -fX```
+ To remove ignored and non-ignored files, run ```git clean -f -x``` or ```git clean -fx```

