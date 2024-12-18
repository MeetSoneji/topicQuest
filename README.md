# **Topic Quest**

### **Overview**
**Topic Quest** is a deep learning-powered platform that extracts and classifies questions from university exam papers. This tool aims to help both students and teachers by creating a topic-wise question bank for various subjects across the university. By leveraging Optical Character Recognition (OCR) and Natural Language Processing (NLP) techniques, Topic Quest provides a convenient way to organize and access past exam questions.

### **Features**
- **PDF/Image Question Extraction**: Automatically extracts questions from exam papers available in PDF or image formats.
- **Topic-wise Classification**: Uses machine learning algorithms to classify questions by subject topic.
- **Question Bank Creation**: Organizes questions into a searchable database for students and teachers.
- **User-friendly Web Interface**: Accessible via a web interface where users can browse questions by year, topic, or subject.
- **Scalable Architecture**: Built to handle multiple subjects and large datasets efficiently.

### **Project Scope**
The goal is to provide a publicly accessible platform that enables students and teachers to:
- Easily search for questions by topic or year.
- Prepare for exams based on past questions.
- Generate a customizable question set for study or assessment purposes.

The project is intended to cover all subjects in the university and will be hosted online for free access.

---

## **Table of Contents**
1. [Project Setup](#project-setup)
2. [Technology Stack](#technology-stack)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Development Roadmap](#development-roadmap)

---

## **Project Setup**
This is an initial setup of the project, and as development progresses, the following components will be added:
- Backend: **Deep Learning Models** for OCR and Classification.
- Frontend: **User Interface** for search, question browsing, and topic-based filtering.
- Database: **Storage** for questions, categorized by topics and subjects.

---

## **Technology Stack**
The project leverages the following technologies:

- **Deep Learning**: TensorFlow, Keras, or PyTorch for question classification.
- **OCR**: Tesseract or OpenCV for image-to-text extraction.
- **Web Development**: Flask or Django (Backend) and HTML/CSS/JavaScript or React (Frontend).
- **Database**: SQLite or PostgreSQL to store and retrieve the extracted questions.
- **Deployment**: GitHub Pages, Heroku, or AWS for hosting the web platform.

---

## **Installation**
To get started with the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MeetSoneji/TopicQuest.git
   cd TopicQuest
   ```

2. **Install Dependencies**:
   Backend dependencies (Python):
   ```bash
   pip install -r backend/requirements.txt
   ```

   Frontend dependencies (optional if using React or another framework):
   ```bash
   npm install
   ```

3. **Set Up the Environment**:
   Ensure you have Python installed (3.8+), as well as any necessary libraries for OCR and deep learning.

4. **Run the Application**:
   ```bash
   python backend/app.py  # For the backend server
   npm start              # For the frontend (if applicable)
   ```

---

## **Usage**
Once the application is up and running:
1. **Upload Exam Papers**: Users can upload PDF or image files of exam papers.
2. **Extract Questions**: The system will extract questions using OCR.
3. **Classify Questions**: Questions will be classified into specific topics using NLP models.
4. **Browse or Search**: Users can browse or search the question bank by subject, topic, or year.

---

## **Development Roadmap**
### **Phase 1: Planning & Initial Setup**
- [x] Define the project scope and features.
- [x] Set up the GitHub repository and collaboration tools.
- [x] Initial project structure with backend and frontend folders.

### **Phase 2: Backend Development**
- [ ] Implement OCR for extracting questions from PDFs and images.
- [ ] Develop deep learning models for classifying questions by topic.
- [ ] Set up a database for storing and retrieving questions.

### **Phase 3: Frontend Development**
- [ ] Design a user-friendly web interface for browsing and searching questions.
- [ ] Implement upload functionality for exam papers.
- [ ] Integrate backend with frontend.

### **Phase 4: Testing and Refinement**
- [ ] Test the system on various subjects and exam papers.
- [ ] Optimize performance for large datasets.
- [ ] Collect feedback from users (students and teachers).

### **Phase 5: Deployment**
- [ ] Deploy the project on GitHub Pages, Heroku, or AWS.
- [ ] Make the platform publicly accessible.


You can update this README as the project grows, adding more details, usage instructions, and development progress. Does this look good to start with?
