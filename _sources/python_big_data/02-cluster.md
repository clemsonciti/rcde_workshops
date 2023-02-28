---
title: "Launching the Spark cluster"
teaching: 0
exercises: 0
questions:
- "How do I launch a Spark cluster at scale of Palmetto?"
objectives:
- "Be able to launch the local Spark cluster"
keypoints:
- "Dynamic Spark clusters can be deployed on Palmetto using provided scripts."
---

> ## 1. Launching the Spark cluster
> 
> - Inside the terminal tab from the `Setup` step, run the following commands:
> 
> ~~~
> $ cd ~/myspark
> $ ./download_spark.sh
> $ ./launch_spark_cluster.sh
> ~~~
>
> - The final output will look similar to the screenshot below (the nodes will be 
> different) .
>
> <img src="../fig/02-cluster/01.png" alt="Spark" style="height:400px">
>
{: .slide}

> ## 2. Summary of executed scripts
> 
> - `download_spark.sh`: Untar a copy of `spark 2.4.5` in `~/software` and 
> install the necessary `pyspark` module for Python. 
> - `launch_spark_cluster.sh`: Parse information from the PBS job, use the first
> node as the Spark master and the remaining nodes as Spark workers. Information 
> regarding the total number of workers, number of cores, and memory per workers 
> are reported for notebook's usage. 
>
{: .slide}

{% include links.md %}

