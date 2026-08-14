PhishGuard-AI-Intelligent-Phishing-Detection

📌 Project Overview

Phishing Website Detection is an Artificial Intelligence and Machine Learning-based project that detects whether a given website URL is Phishing or Legitimate.

Phishing websites are fake websites designed to look like genuine websites in order to trick users into sharing sensitive information such as usernames, passwords, banking details, and personal information.

This project analyzes different URL-based features and uses a trained Machine Learning classification model to predict whether a website is phishing or legitimate.

🎯 Objectives

- Detect phishing websites automatically.
- Extract useful features from website URLs.
- Preprocess URL data for Machine Learning.
- Train a classification model using phishing and legitimate URLs.
- Predict whether a given URL is Phishing or Legitimate.
- Provide a fast and simple phishing detection system.
- Improve awareness and online security.

⚙️ Technologies Used

- Programming Language: Python
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Streamlit / Python Web Application
- Pickle
- GitHub

📂 Project Structure

Phishing-Website-Detection/
│
├── app.py
├── train_model.py
├── phishing_model.pkl
├── requirements.txt
└── README.md

File Description

File| Description
"app.py"| Runs the phishing website detection application
"train_model.py"| Trains the Machine Learning model
"phishing_model.pkl"| Saved trained Machine Learning model
"requirements.txt"| Contains required Python libraries
"README.md"| Project documentation

🔍 Features Used

The system analyzes URL-related characteristics such as:

- URL length
- Number of dots
- Special characters
- Subdomains
- HTTPS usage
- IP address presence
- Redirects
- Suspicious URL patterns
- Domain-related features

These features are used by the Machine Learning model to identify suspicious URLs.

🔄 Working Process

User enters Website URL
          ↓
URL Validation
          ↓
Feature Extraction
          ↓
Data Preprocessing
          ↓
Trained ML Model
          ↓
Prediction
     ↙           ↘
Phishing      Legitimate

🤖 Machine Learning Models

Different classification algorithms can be used for phishing detection, including:

- Random Forest
- Decision Tree
- Logistic Regression
- Support Vector Machine (SVM)

The project report describes these models as part of the implementation and testing process.

🚀 Installation

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the Project Folder

cd Phishing-Website-Detection

3. Install Required Libraries

pip install -r requirements.txt

▶️ Run the Application

If your application uses Streamlit:

streamlit run app.py

Then open the URL displayed in the terminal/browser.

🧪 Example

Enter a website URL into the application.

The system processes the URL and displays one of the following results:

Prediction: Phishing Website

or

Prediction: Legitimate Website

📊 Applications

This project can be useful for:

- Online banking security
- E-commerce website protection
- Social media security
- Email and message link checking
- Educational and organizational networks
- Browser-based security tools

⚠️ Limitations

- The prediction depends on the quality of the training dataset.
- Newly created phishing websites may not always be detected.
- URL-based features alone may not identify every type of phishing attack.
- The model should be regularly updated with new phishing and legitimate URL data.

🔮 Future Enhancements

Future improvements can include:

- Real-time phishing detection
- Browser extension integration
- Larger and regularly updated datasets
- Advanced Machine Learning and Deep Learning models
- Real-time URL reputation checking
- Improved user interface
- Integration with security tools

These enhancements are also consistent with the project's stated future direction.

👩‍💻 Team

AI Career for Women – Engineer Spoke

Project Title

Phishing Website Detection

Team Members

- G. Siri Mahalakshmi
- S. Sirisha
- A. Divyajyothi

Guide

Mr. Abdul Aziz Md

📜 Conclusion

The Phishing Website Detection project demonstrates how Artificial Intelligence and Machine Learning can be applied to a real-world cybersecurity problem. By analyzing URL features and identifying suspicious patterns, the system provides an automated approach for classifying websites as phishing or legitimate.

---

© 2026 Phishing Website Detection Project
