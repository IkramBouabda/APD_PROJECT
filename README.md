# 📝 QCM App

Welcome to **QCM App**, an intuitive Python-based application that lets you manage quizzes interactively via the console. Designed for simplicity and user-friendliness, this tool is perfect for students, educators, or anyone who loves quizzes! 🎉

---

## 🌟 Main Features

- 🚀 **Add New Questions:** Easily add questions and answers to your quiz database.
- 📜 **Review Questions:** View and edit the questions stored in your app.
- 📊 **Take Quizzes:** Test your knowledge with a dynamic QCM experience.
- 🎨 **Enhanced Console Interface:** Leveraging `colorama` and `rich` for a visually appealing experience.

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/IkramBouabda/AP_PROJECT.git
   cd AP_PROJECT
   ```
2. **Install Dependencies**
   Ensure you have Python 3.7+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   python main.py
   ```

## 🌟 All Features

- User Management:

  - Register new users
  - Display previous scores and test dates for returning users
  - Save user data in JSON
  - timer for each question

- Question and Answer Management:

  - Store questions and options in a structured JSON file
  - Validate user answers and compute a score
  - Export results : export user scores to a text file 'user_results.txt' for easy tracking

- Feedback and Scoring:

  - Provide feedback for each question
  - Display the correct answer for incorrect responses
  - Show the final score at the end of the test

## 🎮 How to Use

`1`-**Launch the App**
Run the app in your terminal to start.

`2`-**Enter your id (or both id and username if you are new)** 

`3`-**Choose a category **

`4`-**Then the test starts!**

**Interactive Experience**

- Follow on-screen instructions for a smooth experience.
- Enjoy a colorful and responsive console interface!

---
## :pencil:  How to add questions

`1`-**Launch 'Questions_management.py'**
Run in your terminal to access the management menu.

`2`-**Choose a option **
      - Add Question : to add a new question to any category.
      - Display Questions : a table will be displayed showing questions in each category.
      - Save Questions : to make sure that the questions are added successfully.
      - Exit

## 🛑 Dependencies

This application requires the following Python libraries to run smoothly:

- 🎨 **[colorama](https://pypi.org/project/colorama/)**: Adds beautiful colors to your console output, making the interface more user-friendly.
- 📋 **[rich](https://pypi.org/project/rich/)**: Enhances the console with visually appealing tables, rules, and formatted text.

---

### 📦 Installation

Install all the required dependencies by running the following command in your terminal:

         pip install -r requirements.txt

## 📂 Project Structure

       AP-PROJECT/
       │
       ├── main.py                    # Entry point for the application
       |__ QCM/
       |   ├── testAdministaration.py # Logic for running quizzes
       ├── Questions/
       │   ├── question_manager.py    # Logic for managing questions
           ├── questions.json
       ├── Users
       |   ├── User_management.py     # Logic for managing users
           ├── User_data.json
       ├── user.results.txt           # File to store user quiz results
       ├── requirements.txt           # Python dependencies
       ├── user_results.txt           # user results so he can check them directly 
       └── README.md                  # Project documentation

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:

1.Fork the repository.

2.Create a feature branch:

          git checkout -b feature/new-feature

3.Commit changes:

         git commit -m "Add new feature"

4.Push to the branch:

         git push origin feature/new-feature

5.Open a pull request.

## 📧 Contact

For questions or suggestions, feel free to reach out:

GitHub: rymaatb IkramaBouabda Benhaikmeriem1

Email: rymaaitbraham@gmail.com
