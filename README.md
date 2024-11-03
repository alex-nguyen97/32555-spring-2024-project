# 32555-spring-2024-project

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/alex-nguyen97/32555-spring-2024-project.git
   ```
2. Navigate to the project directory
   ```
   cd 32555-spring-2024-project
   ```
3. Create env file 
   ```
   cp .env.example .env
   ```
4. Installed the required packages
   ```
   pip install tabulate
   pip install dotenv
   pip install customtkinter
   ```

5. Run 
   ```
   python3 main.py
   ```

## Usage

#### Developer mode (optional)
1. Optional: to enable the developer mode. Change ENVIRONMENT in .env to dev: 
   ```
   ENVIRONMENT = 'dev'
   ```
2. Change the rest of the file as the steps that you want to by pass. 

#### Production mode
1. DO NOT delete the CONTENT of students.json (You can delete the file but not the content of it).

2. At the terminal of the main folder, run: 
   ```
   python3 main.py
   ```

## Features
As in https://canvas.uts.edu.au/courses/32394/assignments/191122

## Contributing

Contribution of Group Members 
#### Thai Hung Nguyen - 25608100
1. System architecture and design: Thai Hung did the basic structure of the application. He designed the architecture of the application; for example, how the different sub-systems—Student, Admin, Subject Enrollment, and GUI—would interact with each other to realize a modular and integrated program. That means, defining the classes, methods, and file structure in such a way that it should easily support every component independently as well as smoothly integrate into the larger system. 

2. GUIUniApp Development: Thai Hung implemented the main interface of GUIUniApp, including creating layouts for the Main Windows: login, enrollment, subject listing, and exception handling. He continued to ensure that the layout and design of the GUI are user-friendly, intuitive, and in tune with the functionalities as specified in the CLI version. This translation of CLI commands into GUI buttons and input fields enables users to navigate through screens with ease, thus providing a seamless user experience. 

3. File management and database interaction: Similarly, the file handling features were developed by Thai Hung as part of their architecture. They ensured that the created students.data file, if it does not already exist, managed reads and writes with regard to student and subject information with correct data presentation after each session. The same needed careful handling in order to avoid loss and damage to data. 

4. Integration of the Systems: Thai Hung took it upon himself to carry out the integration of every subsystem such as Student, Admin, and Subject Enrolment with the GUIUniApp. They conducted the final integration and tested every component in the GUI to make sure the components could work together and ran smoothly. This included debugging any issues which arose when they switched from CLI to GUI. 

 

#### Karishma Kumar - 24897314
1. Student System Development: The key activity of Karishma was the implementation of a Student System that included student registration, login, and validation. She has implemented email format validation using Regex, essentially checking the ending @university.com, password format for specific character patterns at correct positions, ensuring that only valid credentials are allowed, thus maintaining data integrity and security. 

2. Testing and Debugging: Karishma led the testing of the project. She was concerned with the debugging of the Student System first and gradually started expanding her work in testing to other systems. Indeed, she has conducted both unit testing—which concerns independently taken functions—and integration testing—across the systems—for smooth functionality. By identifying and fixing these issues, Karishma was able to enhance reliability features in the code to meet specifications presented in the sample I/O. 

3. I/O Matching: Karishma did test how the I/O in terms of wording and indentations was done as per the sample output after the guidelines are provided. This may involve changing outputs to suit exact formats, such as making messages uniform, prompts, and the overall user interface. This is critical in reinforcing the obtaining of full marks in the "Matching I/O" category of the marking scheme. 

#### Yaser Malkawi - 24897466
1. Admin System Development: Yaser developed the Admin System by implementing the functionality that an admin user will need. He has implemented the functionalities of listing all the students, grouping of students based on grade, partitioning of students into pass/fail categories, deletion of any student by their ID, and clearing of all the student data from the system. Yaser has ensured that each function operates as specified, with correct data management and appropriate edge case handling, for example deleting a student which does not exist. 

2. Documentation: Yaser did the documentation,from describing the components to all system functionalities in detail. Also, it described what the purposes are and how each subsystem works, outlined data handling procedures, summarized error-handling mechanisms, and explained every member's contribution in the group for clear and fair accounting of the role of each person in the project. 

3. Final Review of Documentation: After the initial documentation, Yaser worked further with his team on finalizing this review. The suggestions by Thai Hung, Karishma, and Janil were taken into consideration in an aim to make sure the documentation is complete, clear, and concise. This further refined the document to fully align with the final implementation of the project, making sure truly informative for assessors. 

 

#### Janil Jain - 24680845
1. Error Handling and Exception Windows: Janil spearheaded error handling on the project, developing strong mechanisms for handling both command-line interface and GUI errors. They created exception windows in GUIUniApp so that cases of invalid input format and any such enrollment attempts that exceeded the maximum limit on subject enrollment were appropriately caught and serviced. These error windows gave users specific feedback on how to make proper corrections. 

2. Development of Subject Enrollment System: Janil was responsible for the development of Subject Enrollment System, which catered for student enrollment for a maximum of four subjects, removal of subjects, listing of enrolled subjects, and viewing grades. Janil also developed the function to calculate grades based on random marks and imposed restrictions on students enrolling in more than four subjects for project compliance. This subsystem communicated with the students.data for coherent data storage and retrieval. 

3. Final debugging and Error Handling: Other than error handling, Janil conducted final debugging on the whole application to make sure that each portion of it would handle errors elegantly and provide valuable feedback to the user. The debugging work of Janil helped in finding out and fixing any remaining issues, therefore enhancing the stability and smoothness of the program. 

#### Overview of Collaboration 
Individual parts were integrated into one functioning system through tight cooperation between all members. Thai Hung and Karishma were in charge of the main backend systems. Lending support to both the backend and frontend aspects are Yaser and Janil. Testing and reviewing others' work to ensure smooth integration and functionality across all parts of the project is each member's responsibility. Also, the team's commitment to making the submission cohesive and polished was underlined by collaborative debugging and reviewing of the final documentation. 

 