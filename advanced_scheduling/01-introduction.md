---
title: "Introduction to Apache Spark"
teaching: 0
exercises: 0
questions:
- "What is Spark?"
- "How is programming done in Spark?"
objectives:
- "Participants will understand the general concept of the MapReduce programming model"
keypoints:
- "Spark provides a framework to support big data analytics via the MapReduce programming
paradigm, unified compute engines, analytics libraries. Spark supports data processing."
---

> ## 1. What is Spark?
>
> - A unified compute engine and a set of libraries for parallel
> data processing on computer clusters.
> - For more information, review [Integration with Spark](https://jupyterhub-on-hadoop.readthedocs.io/en/latest/spark.html) on JupyterHub.
>
> <img src="../fig/01-introduction/01.png" alt="Spark" style="height:400px">
>
{: .slide}

> ## 2. Design philosophy
>
> - `Unified`: Spark supports a wide range of data analytic tasks over the same
> computing engine and a consistent set of APIs.
> - `Computing engine`: Spark handles loading data from storage systems and
> performs computation on the data (in memory) rather than on permanent storage.
> To adhere to the data locality principle, Spark relies on APIs to provide a
> transparent common interface with different storage systems for all applications.
> - `Libraries`: Via its APIs, Spark supports a wide array of internal and
> external libraries for complex data analytics tasks.
>
{: .slide}

> ## 3. A brief history of Spark
>
> - Research project at UC Berkeley AMP Lab in 2009 to address drawbacks of
> Hadoop MapReduce.
> - Paper published in 2010: [Spark: Cluster Computing with Working Sets](https://static.usenix.org/events/hotcloud10/tech/full_papers/Zaharia.pdf)
> - Source code is contributed to Apache in 2013. The project had more than 100
> contributors from more than 30 organizations outside UC Berkeley.
> - Version 1.0 was released in 2014.
> - Currently, Spark is being used extensively in academic and industry work
> (NASA, CERN, Uber, Netflix …).
>
{: .slide}

> ## 4. map and reduce
>
> - What is `map`? A function/procedure that is applied to every individual
> element of a collection/list/array/…
>
> ~~~
> int square(x) { return x*x;}
> map square [1,2,3,4] -> [1,4,9,16]
> ~~~
> {: .language-bash}
>
> - What is “reduce”? A function/procedure that performs an operation on a list.
> This operation will “fold/reduce” this list into a single value (or a smaller
> subset).
>
> ~~~
> reduce ([1,2,3,4]) using sum -> 10
> reduce ([1,2,3,4]) using multiply -> 24
> ~~~
> {: .language-bash}
>
{: .slide}

> ## 5. MapReduce programming paradigm
>
> - Programmers must implement:
>   - Map function: Take in the input data and return a (key,value) pair.
>   - Reduce function: Receive the (key,value) pairs from the mapper and provide a
>   final output as a reduction operation on the pairs.
>
> - MapReduce framework handles everything else.
> - Spark implements a MapReduce framework.
>
{: .slide}

> ## 6. WordCount: the Hello, World! of Big Data
>
> - WordCount counts how many unique words there are in a file/multiple files.
> - WordCount implements a standard parallel programming approach:
>   - Count number of files
>   - Set number of processes
>   - Possibly set up dynamic workload assignment
>   - A lot of data transfer
>   - Significant coding effort
>
> > ## MapReduce workflow
> >
> > <img src="../fig/01-introduction/02.png" alt="Spark" style="height:400px">
> {: .slide}
>
> > ## MapReduce framework
> >
> > <img src="../fig/01-introduction/03.png" alt="Spark" style="height:400px">
> {: .slide}
{: .slide}


{% include links.md %}

