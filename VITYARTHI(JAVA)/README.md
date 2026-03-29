Campus Course & Records Manager (CCRM):

CCRM is a console-based Java tool for managing the essentials of higher education data. It handles students, courses,     enrollments, and grades, and keeps everything safe with reliable file operations.

Project Overview:
This project is a practical showcase of both basic and advanced Java skills. You’ll see object-oriented programming, modern APIs, and file handling woven into one functional app.
What you can do:
- Student Management: Create, list, update, and deactivate students.
- Course Management: Add and edit courses, deactivate them, and assign instructors.
- Enrollment & Grading: Control enrollments so credit limits aren’t exceeded; manage grades and GPA calculations.
- File Operations: Import/export data as CSV files using NIO.2 for modern file handling.
- Backup System: Make timestamped backups, including deep directory operations, to secure your data.
- System Reports: Get stats and reports for a broad overview.

A Brief Java History:

Java keeps evolving to meet the needs of developers. Here’s how things unfolded:
- 1995: Java 1.0 arrived, introducing “Write Once, Run Anywhere” (WORA).
- 1997: Java 1.1 launched features like inner classes and JDBC.
- 1998: Java 2 (J2SE, J2EE, J2ME) split the platform into Standard, Enterprise, and Micro Editions.
- 2004: Java 5 (J2SE 5.0) brought generics, enums, and the enhanced for-loop.
- 2014: Java 8 shook things up with lambda expressions and the Streams API, bringing functional programming to Java.
- 2017: Java 9 added the Java Platform Module System (JPMS), modularizing the JDK.
- 2018: Java 11 became LTS under the new release schedule, pruning some old Enterprise Java modules.
- 2023: Java 21 released with virtual threads and improved pattern matching.

Java Platforms Explained
- Java SE: Core APIs for desktop, server, and embedded development—CCRM uses this.
- Java EE: For big enterprise systems; provides APIs for servlets, JSPs, web services.
- Java ME: Tailored for mobile and embedded devices with limited resources.

Java Architecture: JDK, JRE, JVM

These three are the backbone of Java:
- JDK (Java Development Kit): Your full toolset—compiler, debugger, and utilities to build Java programs.
- JRE (Java Runtime Environment): Lets you run Java programs; includes the JVM and class libraries, but not development tools.
- JVM (Java Virtual Machine): Converts platform-independent bytecode into code your computer understands—making “Write Once, Run Anywhere” reality.

Getting Started
Prerequisites:
- Java 8 or later
- Any Java IDE (Eclipse, IntelliJ IDEA, VS Code)
- Command-line access

 \#\#\#\# Installation & Setup

1\.  Clone or download the project  
    'git clone \<repository-url\>'  
    'cd campus-course-records-manager'

2\.  Compile the project  
    'javac \-d . src/main/java/com/ccrm/\*.java src/main/java/com/ccrm/\*\*/\*.java'

3\.  Run the application  
    'java com.ccrm.CampusCourseRecordsManager'

    
Setting Up in Eclipse IDE
1. Open Eclipse, go to File > Import…
2. Choose Git > Projects from Git (with smart import), click Next.
3. Select Clone URI, paste the repo URL, and click Next.
4. Pick the main branch, click Next.
5. Set your local directory, click Next.
6. Eclipse should auto-recognize it as a Java project. Click Finish.
Once in your workspace, right-click 'CampusCourseRecordsManager.java' in Package Explorer, then choose Run As > Java Application.

Project Requirements Mapping
 core concepts in the code:
- Encapsulation: Private fields + public getters/setters in 'model/Person.java', 'model/Student.java'.
- Inheritance: Abstract 'Person' is the base for 'Student' and 'Instructor'—they share properties and behaviors.
- Abstraction: 'Person' sets abstract methods like 'getRole()' which subclasses must define.
- Polymorphism: 'Person' references hold either a 'Student' or 'Instructor'—makes code flexible.
- Singleton Pattern: The 'DataStore' manages data with a single instance throughout the app.
- Builder Pattern: 'CourseBuilder', 'TranscriptBuilder' let you construct complex objects step by step.
- Custom Exceptions: 'MaxCreditLimitExceededException' delivers precise error handling.
- NIO.2: File operations via 'Path' and 'Files' APIs in 'utils/FileUtils.java', 'utils/BackupUtils.java'.
- Streams: Stream API used for filtering and data processing in 'core/DataStore.java', 'services/StudentService.java'.
- Date/Time API: 'LocalDate' manages dates in 'model/Student.java' and 'model/Enrollment.java'.
- Enums: 'Semester.java', 'Grade.java' set up type-safe constants with data and methods.
- Recursion: Recursive directory functions appear in 'utils/BackupUtils.java'.

Enabling Assertions:
Turn assertions on with the '-ea' flag in your run command. Handy for debugging and internal checks.
Example:
'java -ea com.ccrm.CampusCourseRecordsManager'

