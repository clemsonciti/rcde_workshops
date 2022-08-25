
# CPU Scheduling"
teaching: 0
exercises: 0
questions:
- "How can an illusion of infinite CPU be managed?"
objectives:
- "Understand the assumptions behind FCFS/SJF"
- "Understand the reasoning behind MLFQ rules" 
keypoints:
- "FCFS/SJF operates based on a set of assumptions that are unrealistics in
the real world."
- "MLFQ rules provide an adaptive approach to adjust the scheduling as needed."


> ## 1. What is CPU scheduling?
> 
> - The allocation of processors to processes over time
> - Key to multiprogramming
> - Increase CPU utilization and job throughput by overlapping I/O and computation
> - Different process queues representing different process states 
> (ready, running, block ...)
> - Policies: Given more than one runnable processes, how do we choose which one to 
> run next?
```

> ## 2. Initial set of simple assumptions
> 
> 1. Each job (process/thread) runs the same amount of time.
> 2. All jobs arrive at the same time.
> 3. Once started, each job runs to completion (no interruption in the middle).
> 4. All jobs only use the CPU (no I/O).
> 5. The run time of each job is known.
>
> These are unrealistic assumptions, and we will relax them gradually to see 
> how it works in a real system.
```

> ## 3. First performance metric
> 
> **Average turn around time of all jobs**.
> 
> turn_around_time = job_completion_time - job_arrival_time
```

> ## 4. Algorithm 1: First Come First Server (FCFS/FIFO)
>
> **First Come First Server (FCFS)/ First In First Out (FIFO)**
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> 3 </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> 0 </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> 0 </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - For FCFS, jobs are executed in the order of their arrival. 
> - When jobs with same arrival time arriva, let's assume a simple alphabetic
> ordering based on jobs' names. 
```

> ## 5. FCFS/FIFO in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (3 + 6 + 9) / 3 = 6. 
```

> ## 6. Initial set of simple assumptions
> 
> 1. ~~Each job (process/thread) runs the same amount of time.~~
> 2. All jobs arrive at the same time.
> 3. Once started, each job runs to completion (no interruption in the middle).
> 4. All jobs only use the CPU (no I/O).
> 5. The run time of each job is known.
>
```

> ## 7. Algorithm 1: First Come First Server (FCFS/FIFO)
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> <b>8</b> </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> 0 </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> 0 </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - For first come first server, jobs are executed in the order of their arrival. 
> - When jobs with same arrival time arriva, let's assume a simple alphabetic
> ordering based on jobs' names. 
```

> ## 8. FCFS/FIFO in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (8 + 11 + 14) / 3 = 11. 
```

> ## 9. Algorithm 2: Shortest Job First (SJF)
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> <b>8</b> </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> 0 </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> 0 </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - For SJF, jobs are executed in the order of their arrival. 
> - When jobs with same arrival time arriva, jobs with shorter service time 
> are executed first. 
```

> ## 10. SJF in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (3 + 6 + 14) / 3 = 7.67. 
```

> ## 11. Initial set of simple assumptions
> 
> 1. ~~Each job (process/thread) runs the same amount of time.~~
> 2. ~~All jobs arrive at the same time.~~
> 3. Once started, each job runs to completion (no interruption in the middle).
> 4. All jobs only use the CPU (no I/O).
> 5. The run time of each job is known.
>
```

> ## 12. Algorithm 1: FCFS/FIFO
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> <b>8</b> </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> <b>2</b> </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> <b>2</b> </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - For FCFS, jobs are executed in the order of their arrival time.
> - When jobs with same arrival time arrive, let’s assume a simple 
> alphabetic ordering based on jobs’ names. 
```

> ## 13. FCFS/FIFO in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (8 + 9 + 12) / 3 = 9.67. 
> - B and C suffer from a long waiting time, but A already got the CPU. 
```

> ## 14. Initial set of simple assumptions
> 
> 1. ~~Each job (process/thread) runs the same amount of time.~~
> 2. ~~All jobs arrive at the same time.~~
> 3. ~~Once started, each job runs to completion (no interruption in the middle).~~
> 4. All jobs only use the CPU (no I/O).
> 5. The run time of each job is known.
>
```

> ## 15. Preemptive vs Non-preemptive
> 
> - Non-Preemptive Scheduling
>   - Once the CPU has been allocated to a process, it keeps the CPU 
>   until it terminates or blocks.
>   - Suitable for batch scheduling, where we only care about the total 
>   time to finish the whole batch.
> - Preemptive Scheduling
>   - CPU can be taken from a running process and allocated to another 
>   (timer interrupt and context switch).
>   - Needed in interactive or real-time systems, where response time 
>   of each process matters.
>
```

> ## 16. Algorithm 3: Shortest Time-to-Completion First (STCF)
>
> Also known as **Preemptive Shortest Job First (PSJF)**
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> 8 </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> <b>2</b> </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> <b>2</b> </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - For FCFS, jobs are executed in the order of their arrival time.
> - When jobs with same arrival time arrive, let’s assume a simple 
> alphabetic ordering based on jobs’ names. 
```

> ## 17. STCF/PSJF in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (14 + 3 + 6) / 3 = 7.67. 
```

> ## 18. Second performance metric
> 
> **Average response time of all jobs**.
>
> The time from when the job arrives to when it is first scheduled. 
>
> response_time = first_scheduled_time - job_arrival_time
>
```

> ## 19. STCF/PSJF in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_response_time = (0 + 0 + 3) / 3 = 1 
```

> ## 20. Algorithm 4: Round Robin (RR)
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> Service Time </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> <b>8</b> </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> <b>2</b> </td>    
>       <td> 3 </td> 
>     </tr>
>     <tr>
>       <td> C </td>
>       <td> <b>2</b> </td>
>       <td> 3 </td> 
>     </tr>
>   </tbody>
> </table>
>
> - All jobs are placed into a circular run queue.
> - Each job is allowed to run for a time quantum `q` before
> being preempted and put back on the queue. 
> - Example: `q=1` 
```


> ## 21. RR in action
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td>  </td>
>       <td>  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#c484ae"> C </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_response_time = (0 + 0 + 1) / 3 = 0.33 
```

> ## 22. Algorithm 4: Round Robin (RR)
> 
> The choice of `q` is important. 
>
> - If `q` becomes infinite, RR becomes non-preemptive FCFS.
> - If `q` becomes 0, RR becomes simultaneously sharing of 
> process (not possible due to context switching).
> - `q` should be a multiple of the timer interrupt interval
>
```

> ## 23. Initial set of simple assumptions
> 
> 1. ~~Each job (process/thread) runs the same amount of time.~~
> 2. ~~All jobs arrive at the same time.~~
> 3. ~~Once started, each job runs to completion (no interruption in the middle).~~
> 4. ~~All jobs only use the CPU (no I/O).~~
> 5. The run time of each job is known.
>
```

> ## 24. (Almost) all processes perform I/O
> 
> - When a job is performing I/O, it is not using the CPU. 
> In other words, it is blocked waiting for I/O to complete.
> - It makes sense to use this time to run some other jobs. 
>
```

> ## 25. Jobs with I/O
>
> <table>
>   <thead>
>     <tr>
>       <th> Job </th>
>       <th> Arrival Time </th>
>       <th> CPU Time </th>
>       <th> I/O </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> A </td>
>       <td> 0 </td>
>       <td> 5 </td>
>       <td> One per 1 sec </td>
>     </tr>
>     <tr>
>       <td> B </td>
>       <td> 0 </td>    
>       <td> 5 </td> 
>       <td> none </td>
>     </tr>
>   </tbody>
> </table>
>
```

> ## 26. Normal STCF treating A as a single job
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (9 + 14) / 2 = 11.5
> - Average_response_time = (0 + 9) / 2 = 4.5
```

> ## 27. STCF treating A as 5 sub-jobs
>
> <table>
>   <thead>
>     <tr>
>       <th> 0 </th>
>       <th> 1 </th>
>       <th> 2 </th>
>       <th> 3 </th>
>       <th> 4 </th>
>       <th> 5 </th>
>       <th> 6 </th>
>       <th> 7 </th>
>       <th> 8 </th>
>       <th> 9 </th>
>       <th> 10 </th>
>       <th> 11 </th>
>       <th> 12 </th>
>       <th> 13 </th>
>       <th> 14 </th>
>       <th> 15 </th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td bgcolor="#db9ec9"> I/O </td>
>       <td bgcolor="#c6c787"> A </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>     <tr>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td bgcolor="#dbdbd3">  </td>
>       <td bgcolor="#8bb3cc"> B </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>       <td>  </td>
>     </tr>
>   </tbody>
> </table>
>
> - Average_turn_around_time = (9 + 10) / 2 = 9.5
> - Average_response_time = (0 + 1) / 2 = 0.5
```

> ## 28. Initial set of simple assumptions
> 
> 1. ~~Each job (process/thread) runs the same amount of time.~~
> 2. ~~All jobs arrive at the same time.~~
> 3. ~~Once started, each job runs to completion (no interruption in the middle).~~
> 4. ~~All jobs only use the CPU (no I/O).~~
> 5. ~~**The run time of each job is known.**~~
>
> The worst assumption:
> - Most likely never happen in real life
> - Yet, without it, SJF/STCF becomes invalid. 
```

> ## 29. The question
> 
> How do we schedule jobs **without knowing** their run time
> duration so that we can minimize **turn around time** and 
> also minimize **response time** for interactive jobs?
```

> ## 30. Multi-level Feedback Queue (MLFQ)
> 
> - Invented by Fernando Jose Corbato (1926 - )
>   - Ph.D. in Physics (CalTech)
>   - MIT Professor
> - One of the original developers of Multics (Predecessor of UNIX)
> - First use of password to secure file access on computers. 
> - Recipient of the 1990 Turing Award (The Nobel prize in computing)
```

> ## 31. Multi-level Feedback Queue (MLFQ)
> 
> - Learn from the past to predict the future
>   - Common in Operating Systems design. Other examples include 
>   hardware branch predictors and caching algorithms.
>   - Works when jobs have phases of behavior and are predictable.
> - Assumption: Two categories of jobs
>   - Long-running CPU-bound jobs
>   - Interactive I/O-bound jobs
```

> ## 32. Multi-level Feedback Queue (MLFQ)
> 
> - Consists of a number of distinct **queues**, each assigned a 
> different **priority level**.
> - Each queue has **multiple** ready-to-run jobs with the **same** priority.
> - At any given time, the scheduler choose to run the jobs in the **queue** 
> with the highest priority
> - If **multiple** jobs are chosen, run them in **Round-Robin**
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-01.png" alt="MLFQ" style="height:300px">
```

> ## 32. Multi-level Feedback Queue (MLFQ): Feedback?
> 
> - Rule 1: If Priority(A) > Priority(B), A runs and B doesn't
> - Rule 2: If Priority(A) == Priority(B), RR(A, B)
> 
> Does it work **well**?
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-01.png" alt="MLFQ" style="height:300px">
```

> ## 33. Multi-level Feedback Queue (MLFQ): Feedback?
> 
> - Rule 1: If Priority(A) > Priority(B), A runs and B doesn't
> - Rule 2: If Priority(A) == Priority(B), RR(A, B)
> 
> With only these two rules, A and B will keep alternating via RR, 
> and C and D will never get to run.  
>
> What other rule(s) do we need to add?  
> - We need to understand how job **priority** changes over time.
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-01.png" alt="MLFQ" style="height:300px">
```

> ## 34. Attempt 1: How to change priority?
> 
> - Rule 3: When a job enter the system, it is placed at the 
> highest priority (the top most queue).
> - Rule 4a: If a job uses up an entire time slice while running, 
> its priority is reduced (it moves down one queue).
> - Rule 4b: If a job gives up the CPU (voluntarily) before the 
> time slice is up, it stays at the same priority level.
>
```

> ## 35. Example 1: A single long-running job
> 
> - System maintains three queues, in the order of 
> priority from high to low: Q2, Q1, and Q0. 
> - Time-slice of 10 ms
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-02.png" alt="MLFQ" style="height:300px">
```

> ## 36. Example 2: Along came a short job
> 
> - Job A (Dark): long-running CPU intensive 
> - Job B (Gray): short-running interactive
>
> Major goal of MLFQ: At first, since the scheduler does not 
> know about the job, it first assumes that is might be a short 
> job (higher priority). If it is not a short job, it will 
> gradually be moved down the queues.
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-03.png" alt="MLFQ" style="height:300px">
```

> ## 36. Example 3: What about I/O?
> 
> - The interactive job (gray) only needs the CPU for 1 ms before 
> performing an I/O. MLFQ keeps B at the highest priority before 
> B keep releasing the CPU.
> - What are potentially problems?
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-04.png" alt="MLFQ" style="height:300px">
```

> ## 37. Problem 1: Starvation
> 
> - If new interactive jobs keep arriving, long running job will 
> stay at the bottom queue and never get any work done. 
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-05.png" alt="MLFQ" style="height:300px">
```

> ## 38. Problem 2: Gaming the system
> 
> - What if some industrious programmers intentionally write a 
> long running program that relinquishes the CPU just before the 
> time-slice is up (Job B). 
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-06.png" alt="MLFQ" style="height:300px">
```

> ## 39. Problem 3: What if a program changes behavior?
> 
> - Starting out as a long running job
> - Turn into an interactive job
>
```

> ## 39. Attempt 2: Priority boost
> 
> Rule 5: After some time period `S`, move all the jobs in the system to 
> the topmost queue.
>
```

> ## 40. Problem: Starvation
> 
> Rule 5 help guaranteeing that processes will not be 
> staved. It also helps with CPU-bound jobs that become interactive
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-07.png" alt="MLFQ" style="height:300px">
```

> ## 41. What S should be set to?
> 
> > ## Voodoo constants (John Ousterhout)
> > S requires some form of magic to set them correctly. 
> > - Too high: long running jobs will starve
> > - Too low: interactive jobs will not get a proper share of the CPU. 
> ```
```

> ## 42. Attempt 3: Better accounting
> 
> - Rewrite of Rule 4 to address the issue of gaming the system. 
> - Rule 5: Once a job uses up its time allotment at a given level 
> (regardless of how many time it has given up the CPU), its priority 
> is reduced. 
>
> <img src="../assets/figure/cpu-scheduling/cpu-scheduling-08.png" alt="MLFQ" style="height:300px">
```

> ## 43. Summary
> 
> - Rule 1: If Priority(A) > Priority(B), A runs (B doesn’t)
> - Rule 2: If Priority(A) = Priority(B), RR(A, B)
> - Rule 3: When a job enter the system, it is placed at the highest priority 
> (the top most queue).
> - Rule 4: Once a job uses up its time allotment at a given level 
> (regardless of how many time it has given up the CPU), its priority 
> is reduced. 
> - Rule 5: After some time period S, move all the jobs in the system to 
> the topmost queue.
>
> MLFQ observes the execution of a  job and gradually learns what type of job 
> it is, and prioritize it accordingly. 
> - Excellent performance for interactive I/O bound jobs: good response time.
> - Fair for long-running CPU-bound jobs: good turnaround time without starvation.
>
> Used by many systems, including FreeBSD, MacOS X, Solaris, Linux 2.6, and Windows NT
```

{% include links.md %}

