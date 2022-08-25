# CSC 468: Introduction to Cloud Computing

> ## Instructor
> - **Instructor**: Linh B. Ngo
> - **Office**: UNA 138
> - **Office Hours**: 
>   - TR: 10:00AM - 12:00PM (in office)
>   - F:  10:00AM - 12:00PM (Zoom - information will be posted in D2L)
> - **Email**: lngo AT wcupa DOT edu
> - **Phone**: 610-436-2595
{: .prereq}


> ## Course Description
> This course provides an introductory overview to the technologies that enable cloud 
> computing. Topics covered include basic concepts about cloud computing, and advanced 
> technical concepts regarding virtualization, containerization, and orchestration.
>
{: .prereq}

> ## Learning Objectives
> <table>
>   <thead>
>     <tr>
>       <th> Course Level Student Learning Outcomes (SLO) </th>
>       <th> CS/ABET Program Outcomes </th>
>       <th> CS Program Objectives </th>
>       <th> Assessment </th>    
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td> 1. Be able to formulate the definition of cloud computing based on essential characteristics, service models, and deployment models </td>
>       <td rowspan="3"> 1. Analyze a complex computing problem and to apply principles of computing and other relevant disciplines to identify solutions (ABET 1). </td>
>       <td rowspan="7"> 1. Be able to apply theory, techniques, and methodologies to create and/or maintain high quality computing systems that function effectively and reliably in the emerging and future information infrastructure.</td>
>       <td> Quiz, Exam </td>     
>     </tr>
>     <tr>
>       <td> 2. Be able to understand enabling technologies including virtualization, containerization, and orchestration. </td>
>       <td> Lab, Project, Quiz, Exam </td>     
>     </tr>
>     <tr>
>       <td> 3. Be able to understand various aspects of cybersecurity in the cloud and of the cloud. </td>
>       <td> Lab, Quiz, Exam </td>
>     </tr>
>     <tr>
>       <td> 4. Be able to deploy various open source cloud computing infrastructures. </td>
>       <td rowspan="2"> 2. Design, implement, and evaluate a computing-based solution to meet a given set of computing requirements in the context of the program’s discipline (ABET 2).  <br> 3. Function effectively as a member or leader of a team engaged in activities appropriate to the program’s discipline (ABET 5). </td>
>       <td> Lab, Quiz, Exam </td>
>     </tr>
>     <tr>
>       <td> 5. Be able to deploy applications in the cloud </td>
>       <td> Lab, Quiz, Exam </td>
>     </tr>
>   </tbody>
> </table>
>
> ### Certificate in Computer Security Program Outcomes
> 1. Analyze and resolve security issues in network and computer systems to secure 
>  an IT infrastructure
> 2. Implement secure measurements to protect networks, secure electronic assets, 
> prevent attacks, ensure privacy, and build secure infrastructures that respect ethical 
> principles. 
>
> ### Course Topics:
>
> - Basic Concepts  
>   - Introduction, Essential Characteristics, and Enabling Technologies
>   - Service Models and Deployment Models
>   - Cloud Infrastructure in Academic: CloudLab
> - Virtualization and Containerization
>   - Introduction to Virtualization in Cloud Computing
>   - KVM, Docker, Podman, and Singularity
>   - CloudLab: Programmatically Deployment of Infrastructure
>   - CloudLab: OpenStack
>   - CloudLab: Podman/Buildah
> - Containers Orchestration
>   - Kubernetes
>
> ### Artifacts used to demonstrate Student Learning Outcomes:
> - Lab: In the lab, students will learn to set up a Linux distribution designed for cloud environment, 
> then deploy the image on an open source cloud infrastructure. 
> - Projects: Students will work as a team and select one of the different aspects of cloud computing 
> to explore.
>   - Implementation and deployment of cloud computing infrastructures.
>   - Performance evaluation of virtualization approaches.
>   - Installation and deployment of computing services in the cloud
> - Quiz and Exams. 
{: .objectives}

> ## Prerequisites
> - CSC 231: Computer Systems
{: .prereq}

> ## Required Text (either print or e-book):
> There is no required text for this class. 
{: .prereq}

> ## Evaluation Policy:
>
> ### Grade Distributions
>
> | Percentage | Tasks |
> | ---------- | ----- |
> | 5% | 1 individual lab |
> | 45% | 1 3-part team project |
> | 20% | 10 Quizzes |
> | 15%  | Midterm Exam |
> | 10% | Final Exam |
> |  5% | Participation |
>
> ### Grade Scale:
>
> | Numeric | Letter |
> | ---------- | ----- |
> | 100-93 |	A |
> | 92-90	| A- |
> | 89-87	| B+ |
> | 86-83	| B |
> | 82-80	| B- |
> | 79-77	| C+ |
> | 76-73	| C |
> | 72-70	| C- |
> | 69-67	| D+ |
> | 66-63	| D |
> | 62-60	| D- |
> | <= 59	| F |
>
> ### Lateness Policy:
> Assignments that are late are assessed a 10% per day late penalty.
> Saturday and Sunday are each days.
{: .keypoints}


> ## Policy
>
> ### University Sanctioned Events Policy:
> Students participating in participating in University sanctioned events such
> as, but not limited to, the Marching Band, musical ensembles, theatre group,
> athletic events, forensics competition, etc., will be granted an excused
> absence for class periods missed. Students will be granted the privilege of
> taking, at an alternative time to be determined by the professor, scheduled
> examinations or quizzes that will be missed. I will designate such times prior
> to the event and reserve the right to provide a fair alternative to taking the
> examination or quiz that will be missed. Students must submit original
> documentation on University letterhead signed by the activity director, coach,
> or adviser detailing the specifics of the event in advance. Specific
> requirements include:
>
> 1. Responsibility for meeting academic requirements rests with the student.
> 2. Students are expected to notify their professors as soon as they know they
> will be missing class due to a University sanctioned event.
> 3. Students are expected to complete the work requirement for each class and
> turn in assignments due on days of the event prior to their due dates unless
> other arrangements are made with myself.
> 4. If a scheduled event is postponed or canceled, the student is expected to
> go to class.
> 5. Students are not excused from classes for practice on nonevent days.
>
> The following are specifics for the student athlete:
> 1. The student athlete is expected, where possible, to schedule classes on
> days and at hours that do not conflict with athletic schedules.
> 2. Athletes are not excused from classes for practice or training-room
> treatment on nongame days.
>
> ### Email Policy:
> It is expected that faculty, staff, and students activate and maintain regular
> access to University provided e-mail accounts. Official university
> communications, including those from your instructor, will be sent through your
> university e-mail account. You are responsible for accessing that mail to be
> sure to obtain official University communications. Failure to access will not
> exempt individuals from the responsibilities associated with this course.
>
> Please abide by the following email etiquette policies to ensure clear
> communication:
> - **Subject Line**:	Please include a descriptive and specific subject heading for
> all of your emails, including course and section number (e.g. “CSC 050-23:
> Question about lab 1”).
> - **Greeting**:	Please make a clear and appropriate greeting; I will not answer
> emails addressed to “hey” or “yo”. Please address me as Dr. Ngo, or “Professor”.
> - **Tone & Style**:	Always use a tone and language that is appropriate to an
> academic setting; I will not respond to emails that are written in short-hand
> or without proper punctuation and grammar. Your emails should not resemble a
> text message.
> - **Sign and Proofread**:	Always sign your full name, especially if you are
> writing from your smart phone. Always proofread your emails before sending.
> - **Email Account**:	I do not care which email account you send email from, as
> long as it is clearly addressed and signed so that I know who you are. But
> please be advised to appropriately link the email that you wish to use with
> myWCU and D2L; I will be using those services to send out emails to the
> entire class. It is your responsibility to make sure this is configured
> correctly so that you receive my emails.
>
> ### Computer Science Department Dishonesty Policy:
> The Computer Science Committee has adopted the following policies in regard
> to academic dishonesty in Computer Science classes:
> 1. A student found to be academically dishonest in an assignment will receive
> zero for that assignment if it is his/her first offense in that class [the
> course, not the class period], but an F for the course if it is for his/her
> second offense in that class [the course].
> 2. A student found to be academically dishonest in a test will receive the
> grade of F in that class [the course].
> 3. For the purposes of this document on academic dishonesty, every form or
> method of evaluation in a class will be considered as being of one of two
> types: an assignment or a test. Assignments include homework assignments, and
> short quizzes [and labs]. Tests include final exams and major exams. An
> instructor has, subject to these guidelines, the discretion to determine the
> type of any other form of evaluation, such as a project, in his/her class.
> 4. A student who has received the grade of F in a course because of academic
> dishonesty and who wants or is required to repeat that course may re-take
> that course only as a regularly scheduled course that is open to the student
> community in general. In exceptional circumstances, this condition may be
> revoked, but only by an explicit action to that effect by the full Computer
> Science Committee, and only then on a case by case basis.
> 5. The term academic dishonesty is used throughout in the sense provided by
> the rules and regulations of West Chester University. The following is taken
> from The Ram's Eye View of 1997-1998: **“Academic dishonesty as it applies to
> students includes but is not limited to academic cheating; plagiarism; the
> sale, purchase, or exchange of term papers or research papers; falsification
> of information which includes any form of providing false or misleading
> information, written, electronic, or oral; or of altering or falsifying
> official institutional records. Plagiarism is defined as copying another's
> work or portion thereof and/or using ideas and concepts of another and
> presenting them as one's own without giving proper credit to the source.”**
>
> ### No-Grade, Violation of Academic Integrity, and Violation of Student Code of Conduct Policy:
> For questions regarding Academic Dishonesty, the No-Grade policy, Sexual
> Harassment, or the Student Code of Conduct, students are encouraged to refer
> to their major department’s handbook, the Undergraduate Course Catalogue, the
> Rams Eye View, or the University Web Site. Please understand that improper
> conduct in any of these areas will not be tolerated and may result in
> immediate ejections from the class.
>
> ### ADA Policy:
> If you have a disability that requires accommodations under the Americans
> with Disabilities Act (ADA), please present your letter of accommodations
> and meet with me as soon as possible so that I can support your success in
> an informed manner. Accommodations cannot be granted retroactively. If you
> would like to know more about West Chester University’s Services for Students
> with Disabilities (OSSD), please contact the OSSD which is located at 223
> Lawrence Center. The OSSD hours of Operation are
> Monday – Friday 8:30 a.m. – 4:30 p.m. Their phone number is 610-436-2564,
> fax number is 610-436-2600, and their email address is [ossd@wcupa.edu](mailto:ossd@wcupa.edu).
> More information can be found at
> the [OSSD website](http://www.wcupa.edu/ussss/ossd).
>
> ### Title IX Statement:
> West Chester University and its faculty are committed to assuring a safe and
> productive educational environment for all students. In order to meet this
> commitment and to comply with Title IX of the Education Amendments of 1972
> and guidance from the Office for Civil Rights, the University requires
> faculty members to report incidents of sexual violence shared by students
> to the University's Title IX Coordinator, Ms. Lynn Klingensmith. The only
> exceptions to the faculty member's reporting obligation are when incidents
> of sexual violence are communicated by a student during a classroom
> discussion, in a writing assignment for a class, or as part of a
> University-approved research project. Faculty members are obligated to
> report sexual violence or any other abuse of a student who was, or is, a
> child (a person under 18 years of age) when the abuse allegedly occurred to
> the person designated in the University protection of minors policy.
> Information regarding the reporting of sexual violence and the resources
> that are available to victims of sexual violence is set forth at the
> [Office of Social Equity website](http://www.wcupa.edu/_admin/social.equity).
>
> ### Emergency Contact:
> In the event of an emergency during class, the phone number for WCU’s
> Department of Public Safety is 610-436-3311.
{: .keypoints}

{% include links.md %}
