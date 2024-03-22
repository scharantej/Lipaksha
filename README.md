## Flask Application Design for a Malayalam Learning Website

**HTML Files:**

1. **index.html:** The main page of the website, welcoming the user and providing an overview of the Malayalam learning course.
2. **lessons.html:** Presents the different lessons available in the course. Each lesson should be a separate section on this page.
3. **lesson1.html**, **lesson2.html**, ...: Individual HTML files for each lesson, containing the content, grammar explanations, exercises, etc.
4. **practice.html:** A dedicated page for learners to practice their Malayalam skills.
5. **quizzes.html:** A page that hosts quizzes to test the learner's understanding.
6. **feedback.html:** A page where learners can provide feedback on the course content.

**Routes:**

1. **@app.route('/')**: The main route, displaying the index.html page.
2. **@app.route('/lessons')**: Displays the lessons.html page, listing the available lessons.
3. **@app.route('/lesson/<lesson_number>')**: Dynamic route that displays the specific lesson page (e.g., /lesson/1 for lesson 1).
4. **@app.route('/practice')**: Displays the practice.html page.
5. **@app.route('/quizzes')**: Displays the quizzes.html page.
6. **@app.route('/feedback')**: Displays the feedback.html page.

**Explanation:**

- The HTML files serve as the building blocks of the website, providing the content and structure to the users.
- The routes define how the application responds to specific URLs. Each route is mapped to an HTML file, allowing the application to display the appropriate content.
- The dynamic route for displaying individual lessons allows users to easily access specific lessons by entering the lesson number in the URL.