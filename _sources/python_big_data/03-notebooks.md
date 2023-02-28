---
title: "Workshop notebooks"
teaching: 0
exercises: 0
questions:
- "How do I launch the workshop notebooks and link them to the Spark cluster?"
objectives:
- "Be able to setup notebooks to connect to the Spark cluster"
keypoints:
- "Understand your Spark cluster configuration to optimize notebooks' resource request."
---

> ## 1. Where are the notebooks
> 
> - The notebooks for this workshop are included inside myspark.
> - Double-click on `myspark` directory in the `File Browser` tab. 
> 
> <img src="../fig/03-notebooks/01.png" alt="Notebooks" style="height:800px">
>
> - We will go through the four notebooks today. 
> - Double-click on `intro-to-pyspark-01.ipynb` to open the first notebook. 
>
> <img src="../fig/03-notebooks/02.png" alt="Notebook 01" style="height:500px">
{: .slide}

> ## 2. Notebook configuration
> 
> - The first code cell of all the notebooks is the same. 
> - This cell sets up the configuration to connect to the launched Spark cluster. 
> - The following three configuration settings should be modified to match what 
> was reported on the terminal (**they are not here**). 
>   - `spark.driver.memory`: value from `Memory per workers`.
>   - `spark.executor.instances`: value from `Num workers`. 
>   - `spark.executor.memory`: value from `Memory per workers`. 
>   - `spark.executor.cores`: value from `Cores per worker`.
>
> <img src="../fig/03-notebooks/03.png" alt="Configuration" style="height:500px">
{: .slide}

> ## 3. Clean up
> 
> Each notebook will open a separate SparkContext on the Spark cluster. This  
> SparkContext must be stopped (last cell of each notebook) when we are done. 
{: .slide}

{% include links.md %}

