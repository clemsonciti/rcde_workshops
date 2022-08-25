# Setup Apache Spark

## Setup Spark on Windows
```{dropdown}
- **Make sure that your Windows is up to date prior to completing the remaining steps**. 
- **If you are running on Windows Home, make sure that you switch out of S mode**.
- The minimal configuration this setup has been tested on is:
  - Intel Celeron CPU N3550
  - 4GB memory
  - Windows 10 Home version 20H2

### Windows Terminal

- Make sure that your computer is updated.    
- I will assume that everyone's computer is running Windows 10, as it is the
standard OS on all Windows-based laptop being sold nowadays. 
- Go to `Microsoft Store` app, search and install `Windows Terminal`. 

<img src="fig/setup/01.png" style="height:400px">

### Install Java 

- It is most likely that you already have Java installed. To confirm this, 
first, open a terminal. 

- Run `javac -version`

~~~
$ javac -version
~~~


- You see the version of Java being displayed on screen. Your version might 
be different from mine.

~~~
javac 1.8.0_222
~~~


- Run `java -version`.

~~~
$ java -version
~~~


- Similarly, version information will be displayed.

~~~
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
~~~


If you do not have **both** `java` and `javac`, you will need to install Java
SDK (Software Development Kit). We will be using the Java distribution maintained
by OpenJDK.

- Go to [OpenJDK website](https://adoptopenjdk.net).
- Choose **OpenJDK 8 (LTS)** for Version and **HotSpot** for JVM.
- Click on the download link to begin download the installation package.
- Run the installer. You can keep all default settings on the installer.
- Once the installation process finishes, carry out the tests above again in another terminal
to confirm that you have both `java` and `javac`.

### Install Anaconda

- Visit [Anaconda's download page](https://www.anaconda.com/products/individual) 
and download the corresponding Anaconda installers. 
- You should select the 64-Bit variety for your installers. 
- Run the installation for Anaconda.
- Remember the installation directory for Anaconda. 
- For Windows, this is typically under `C:\Users\YOUR_WINDOWS_USERNAME\anaconda3`. 
or `C:\ProgramData\anaconda3`.
- Open a terminal and run:

~~~
$ conda init powershell
~~~


- Restart the terminal


### Download Spark

- Download [Spark 3.0.1](https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz) 
- Untar and store the final directory somewhere that is easily accessible. 
- You might need to download and install [7-Zip](https://www.7-zip.org/) to 
decompress `.tgz` file on Windows.
- When decompressing, you might have to do it twice, because the first decompression 
will return a `.tar` file, and the second decompression is needed to completely 
retrieve the Spark directory. 
- Move the resulting directory under the `C:` drive. 

### Install libraries to support Hadoop functionalities

- Open `Windows Terminal`, and create a `hadoop` directory and a `bin` subdirectory
under the `C:` drive.  

~~~
$ cd c:\
$ mkdir -p hadoop\bin
~~~


<img src="fig/setup/03.png" style="height:200px">

- Visit the [link to winutils.exe](https://github.com/cdarlint/winutils/blob/master/hadoop-3.0.1/bin/winutils.exe), right click on the `Download` and choose `Save Link As`. 
- Save the file to `C:\hadoop\bin`.
- Visit the [link to hadoop.dll](https://github.com/cdarlint/winutils/blob/master/hadoop-3.0.1/bin/hadoop.dll), right click on the `Download` and choose `Save Link As`. 
- Save the file to `C:\hadoop\bin`.

<img src="fig/setup/04.png" style="height:700px">


### Setup environment variables


- Click on the Windows icon and start typing `environment variables` in the 
search box. 
- Click on `Edit the system environment variables`.    

<img src="fig/setup/05.png" alt="Open system properties" style="height:400px">

- Click on `Environment Variables`.
- Under `User variables for ...`, click `New` and enter following pairs of input
for each of the items below. Click `OK` when done. 
  - Java
    - `Variable name`: `JAVA_HOME`.
    - `Variable value`: Typically `C:\Program Files\AdoptOpenJDK\jdk-8.0.222.10-hotspot`.
  - Spark
    - `Variable name`: `SPARK_HOME`.
    - `Variable value`: `C:\spark-3.0.1-bin-hadoop3.2`.
  - Hadoop
    - `Variable name`: `HADOOP_HOME`.
    - `Variable value`: `C:\hadoop`.
  - Anaconda3
    - `Variable name`: `ANACONDA_HOME`.
    - `Variable value`: `C:\Users\YOUR_WINDOWS_USERNAME\anaconda3`.

<img src="fig/setup/06.png" style="height:600px">

- In `User variables for ...`, select `Path` and click `Edit`. Next, 
add the executable  and enter following pairs of input by pressing `New` 
to enter each the items below into the list. Click `OK` when done. 
  - Java: `%JAVA_HOME%\bin`
  - Spark: `%SPARK_HOME%\bin`
  - Hadoop: `%HADOOP_HOME%\bin`
  - Anaconda3: `%ANACONDA_HOME%\Scripts`
<img src="fig/setup/07.png" style="height:400px">

- Close your terminal and relaunch it. Test that all paths are setup correctly
by running the followings:

~~~
$ where.exe javac
$ where.exe spark-shell
$ where.exe winutils
~~~


<img src="fig/setup/08.png" style="height:300px">


### Setup Jupyter and pyspark

- Open a terminal and run the followings:

~~~
$ conda create -y -n pyspark python=3.6
$ conda activate pyspark
$ conda install -y -c conda-forge findspark
$ conda install -y ipykernel jupyter numpy
~~~



### Test Jupyter and pyspark

- Download the [following Shakespeare collection](http://www.gutenberg.org/files/100/100-0.txt). 
- Open a terminal
- Launch Jupyter notebook
- Open a new notebook using the `pyspark` kernel. 

~~~
$ conda activate pyspark
$ jupyter notebook
~~~


- Enter the following Python code into a cell of the new notebook.
- Replace `PATH_TO_DOWNLOADED_SHAKESPEARE_TEXT_FILE` with the actual path (including the
file name) to where you downloaded the file earlier. 

<script src="https://gist.github.com/linhbngo/ccfc056504609ee6104a3256088f6b0f.js?file=wordcount.py"></script>

- Adjust the values for `number_cores` and `memory_gb` based on your computer's configuration. 
  - For example, on a computer running Intel Celeron N3550 with 2 logical cores and 4GB of memory, `number_cores` 
  is set to `2` and `memory_gb` is set to `2`. 
- Run the cell. 
- Once (if) the run completes successfully, you can revisit your Jupyter Server
and observe that `output-word-count-1` directory is now created. 
  - `_SUCCESS` is an empty file that serves the purpose of notifying of a successful
  execution. 
  - `part-00000` and `part-00001` contains the resulting outputs. 

<img src="fig/setup/09.png" style="height:350px">
<img src="fig/setup/10.png" style="height:900px">

- You can also visit `127.0.0.1:4040/jobs`, you can observe the 
running Spark cluster spawned by the Jupyter notebook:

<img src="fig/setup/11.png" style="height:500px">

- Changing the Spark page's tab to `Executors`to observe the configuration of the cluster:
  - The cluster has 8 cores
  - The amount of available memory is only 8.4GB out of 16GB, this is due to 
  Spark's memory storage reservation/protection.

<img src="fig/setup/12.png" style="height:500px">

{: .slide}



## Mac Terminal

- Click on the search box at the top right of the screen.    
- Type `Terminal` into the search box. 
- Click on the `Terminal` app that shows up.  

### Install Java 

- It is most likely that you already have Java installed. To confirm this, 
first, open a terminal. 

- Run `javac -version`

~~~
$ javac -version
~~~


- You see the version of Java being displayed on screen. Your version might 
be different from mine.

~~~
javac 1.8.0_222
~~~


- Run `java -version`.

~~~
$ java -version
~~~


- Similarly, version information will be displayed.

~~~
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
~~~


If you do not have **both** `java` and `javac`, you will need to install Java
SDK (Software Development Kit). We will be using the Java distribution maintained
by OpenJDK.

- Go to [OpenJDK website](https://adoptopenjdk.net).
- Choose **OpenJDK 8 (LTS)** for Version and **HotSpot** for JVM.
- Click on the download link to begin download the installation package.
- Run the installer. You can keep all default settings on the installer.
- Once the installation process finishes, carry out the tests above again in another terminal
to confirm that you have both `java` and `javac`.

### Install Anaconda

- Visit [Anaconda's download page](https://www.anaconda.com/products/individual) 
and download the corresponding Anaconda installers. 
- You should select the 64-Bit variety for your installers. 
- Run the installation for Anaconda.
- Remember the installation directory for Anaconda. 
- For Mac, this is typically under `/Users/YOUR_MAC_USERNAME/anaconda3`. 


### Download Spark

- Download [Spark 3.0.1](https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz) 
- Assuming you are using Safari to download, the file will be decompressed into a `.tar` 
file inside `Downloads`. You can completely decompress the file into a directory under 
your home directory as follows:  
 
~~~
$ cd
$ mv PATH_TO_DOWNLOADED_SPARK_FILE .
$ tar xf PATH_TO_DOWNLOADED_SPARK_FILE
~~~


- If you use Chrome and save the file to a different location (no automatic decompression 
via Mac), use `tar xzf ...` instead of `tar xf ...`. 


### Setup environment variables


- Run the following commands to setup your environment variables 

~~~
$ cd
$ echo 'export JAVA_HOME=$(which java | sed "s/\/bin\/java//g")' >> ~/.zprofile
$ echo 'export SPARK_HOME="/users/${USER}/spark-3.0.1-bin-hadoop3.2"' >> ~/.zprofile
$ echo 'export ANACONDA_HOME="/users/${USER}/anaconda3"' >> ~/.zprofile
$ echo 'export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$ANACONDA_HOME/bin:$PATH' >> ~/.zprofile
$ source ~/.bash_profile
~~~


- Test that all paths are setup correctly by running the followings:

~~~
$ which javac
$ which spark-shell
$ which conda
~~~


### Setup Jupyter and pyspark

- Open a terminal and run the followings:

~~~
$ conda create -y -n pyspark python=3.6
$ source activate pyspark
$ conda install -y -c conda-forge findspark
$ conda install -y ipykernel jupyter numpy
~~~



### Test Jupyter and pyspark

- Download the [following Shakespeare collection](http://www.gutenberg.org/files/100/100-0.txt). 
- Open a terminal
- Launch Jupyter notebook
- Open a new notebook using the `pyspark` kernel. 

~~~
$ source activate pyspark
$ jupyter notebook
~~~


- Enter the following Python code into a cell of the new notebook.
- Replace `PATH_TO_DOWNLOADED_SHAKESPEARE_TEXT_FILE` with the actual path (including the
file name) to where you downloaded the file earlier. 

<script src="https://gist.github.com/linhbngo/ccfc056504609ee6104a3256088f6b0f.js?file=wordcount.py"></script>

- Adjust the values for `number_cores` and `memory_gb` based on your computer's configuration. 
  - For example, on a computer running Intel Celeron N3550 with 2 logical cores and 4GB of memory, `number_cores` 
  is set to `2` and `memory_gb` is set to `2`. 
- Run the cell. 
- Once (if) the run completes successfully, you can revisit your Jupyter Server
and observe that `output-word-count-1` directory is now created. 
  - `_SUCCESS` is an empty file that serves the purpose of notifying of a successful
  execution. 
  - `part-00000` and `part-00001` contains the resulting outputs. 

<img src="fig/setup/09.png" style="height:350px">
<img src="fig/setup/10.png" style="height:900px">

- You can also visit `127.0.0.1:4040/jobs`, you can observe the 
running Spark cluster spawned by the Jupyter notebook:

<img src="fig/setup/11.png" style="height:500px">

- Changing the Spark page's tab to `Executors`to observe the configuration of the cluster:
  - The cluster has 8 cores
  - The amount of available memory is only 8.4GB out of 16GB, this is due to 
  Spark's memory storage reservation/protection.

<img src="fig/setup/12.png" style="height:500px">

{: .slide}



## Linux Terminal (instructions provided by Austin Heard - Fall 2021)

- If you have a Linux distro, you really should know how to launch a Terminal. 

### Install Java 

- It is most likely that you already have Java installed. To confirm this, 
first, open a terminal. 

- Run `javac -version`

~~~
$ javac -version
~~~


- You see the version of Java being displayed on screen. Your version might 
be different from mine.

~~~
javac 1.8.0_222
~~~


- Run `java -version`.

~~~
$ java -version
~~~


- Similarly, version information will be displayed.

~~~
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
~~~


If you do not have **both** `java` and `javac`, you will need to install Java
SDK (Software Development Kit). We will be using the Java distribution maintained
by OpenJDK.

- Go to [OpenJDK website](https://adoptopenjdk.net).
- Choose **OpenJDK 8 (LTS)** for Version and **HotSpot** for JVM.
- Click on the download link to begin download the installation package.
- Run the installer. You can keep all default settings on the installer.
- Once the installation process finishes, carry out the tests above again in another terminal
to confirm that you have both `java` and `javac`.

### Install Anaconda

- Visit [Anaconda's download page](https://www.anaconda.com/products/individual) 
and download the corresponding Anaconda installers. 
- You should select the 64-Bit variety for your installers. 
- Run the installation for Anaconda.
- Remember the installation directory for Anaconda. 
- For Linux, this is typically under `/home/YOUR_LINUX_USERNAME/anaconda3`. 


### Download Spark

- Run the following commands:  
 
~~~
$ cd
$ wget https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
$ tar xzf spark-3.0.1-bin-hadoop3.2.tgz
~~~


### Setup environment variables


- Run the following commands to setup your environment variables 

~~~
$ cd
$ echo 'export JAVA_HOME=$(which java | sed "s//bin/java//g")' >> ~/.bashrc
$ echo 'export SPARK_HOME="/home/${USER}/spark-3.0.1-bin-hadoop3.2"' >> ~/.bashrc
$ echo 'export ANACONDA_HOME="/home/${USER}/anaconda3"' >> ~/.bashrc
$ echo 'export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$ANACONDA_HOME/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
~~~


- Test that all paths are setup correctly by running the followings:

~~~
$ which javac
$ which spark-shell
$ which conda
~~~


### Setup Jupyter and pyspark

- Open a terminal and run the followings:

~~~
$ conda create -y -n pyspark python=3.6
$ source activate pyspark
$ conda install -y -c conda-forge findspark
$ conda install -y ipykernel jupyter numpy
~~~


- For the remainder of the instruction to launch Jupyter Notebook/Spark, it is the same as those of Mac. 

{:.slide}

{% include links.md %}