
# Course Project"
teaching: 0
exercises: 0
questions:
- "What is the scope of the project?"
objectives:
- "Identify your team"
- "Identify your project"
- "Identify how hard your team should make your projects"
keypoints:
- "Be fearless"



> ## 1. Introduction
>
> **Enhance** the **design** and **implementation** and carry out the **full stack deployment** 
> (including CI/CD services) of the coin miner design or an alternative design with at least 
> similar level of complexity on CloudLab.
>
```


> ## 2. General requirements
>
> - All projects will be carried out/demonstrated on CloudLab. 
> - All subsequent hands-on in class will be done as part of a team. 
> - Team: 4 to 5 members
```


> ## 3. C-level technical requirements
>
> - Core components: `webui`, `rng`, `hasher`, `worker`, `redis`
> - Inclusion of CI/CD services with demonstrated live update of `webui` display. 
> - Inclusion of a Docker image hub as part of the infrastructure
> - Cosmetic update to `webui`. 
> - Conversion of the infrastructure from using `docker-compose` to `kubernetes` deployment.  
>
```


> ## 4. B-level technical requirements
>
> - Everything from the C-level requirements  
> - Complete replacement of one service design. For example, instead of using `redis`, 
> switch to `mysql`. Instead of using `ruby` for `hasher`, it can be rewritten as Python code or
> another language. 
> - An alternative design will be evaluated on a case-by-case basis using the complexity of coin-miner 
> as the benchmark. 
>
```


> ## 5. A-level technical requirements
>
> - Everything from the C-level requirements  
> - Complete replacement of three or more service design. This most likely will result in the 
> replacement of `redis` with another database solution, and the rewriting/implementation of two 
> of the remaining components. 
>   - Staying with coin-miner will be difficult for getting an A-level evaluation due to the existing 
>   creative limitation of the project itself. 
> - An alternative design with high level of complexity is more likely to achieve an A-level technical
> requirements. 
> - I want this project to be something that will wow your technical interviewers. 
>
```


> ## 6. Project deliverables
>
> - Deliverable 1: 
>   - Team description, including a 2-page resume for each team member. 
>   - A Technical Report with the first two chapters: 
>     - Chapter 1 describes **your team's vision** for the `coin-miner` or a selected alternative. This is 
>     simply a design document (similar to the second figure in slide 1, Introduction to Cloud Computing).
>     - Chapter 2 provides a detailed description about what your team **propose** to do to address 
>     the technical requirements above. 
>    
> - Deliverable 2: (tentatively after Spring Break)
>   - 10-minute in-class demonstration without CI/CD service.
>     - For coin-miner, cosmetic changes (C-level) are expected.  
>   - Brief update on technical challenges/difficulties.  
>   - Prediction on the feasibility of successful completion of the project. 
>   - Updated the Technical Report with Chapter 3 describing the current progress/accomplishment/challenges
>
> - Deliverable 3:
>   - 10-minute in-class presentation of the project
>   - Final chapter of Written Project Report with the project description in full, self-evaluation regarding 
>   whether the project has met all technical requirements specified in Chapter 2. The Reference section must 
>   include link to the GitHub repository of the team project. 
>
```


> ## 7. Technical Report Requirements (strict)
>
> - PDF format only for final submission. Word documents will not be considered. 
> - Cover page with Project Title and Member Names
> - A single page with a short summary that describes the project. 
> - Technical Report (Chapter 1 through 4)
> - Reference page
> - Members' resume
> - Summary and Technical Report must be kept to a 11-point Arial/Time News Roman font, 
> single space, 1-inch margin.
> - Correct grammar, vocabulary, and clear and concise sentences are required. 
>
```




{% include links.md %}

