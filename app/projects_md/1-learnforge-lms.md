# LearnForge LMS

## Summary

A Learning Management System built as a full-stack Ruby on Rails application. LearnForge LMS supports instructors and learners with **role-based access**, **lesson progress tracking**, and **course management**. Demonstrates clean Rails architecture, modern Hotwire-driven interactivity, and professional full-stack development practices including **Test-Driven Development (TDD)**.

[View the code on GitHub](https://github.com/ajtran303/learnforge-lms/)

---

## Highlights

- **Role-based Access & Authentication:** Email/password login using `bcrypt`, with **Learner** and **Instructor** roles enforcing proper authorization throughout the app
- **Course & Lesson Management:**
    - Instructors can create, edit, and delete courses
    - Draft/published workflow for courses
    - Add, edit, and delete lessons
    - Inline lesson editing with Turbo frames
- **Learning Experience for Learners:**
    - Browse published courses only
    - Enroll in courses with one click
    - Track lesson completion and course progress with visual progress bars
    - Navigate lessons via previous/next buttons and sidebar
- **Interactive UI:** Turbo-powered updates for lessons, lesson completion,and course progress without full-page reloads
- **Test-Driven Development:** RSpec & Capybara tests for: courses, lessons,and  enrollment, lesson completion and course progress, role-based access control, and authentication and user registration
- **Responsive Design:** Mobile-friendly layout with smooth interactions

---

## Tech Stack

- **Backend:** Ruby on Rails 8.1
- **Database:** PostgreSQL
- **Frontend:** Turbo, Bootstrap 5
- **Authentication:** `has_secure_password` (bcrypt)
- **Testing:** RSpec, Capybara, Shoulda Matchers
- **Deployment:** Render

---

## Live Demo

Live Demo: [LearnForge LMS](https://learnforge-lms.onrender.com/)

Login with any of the following users:

```
instructor1@example.com    password
instructor2@example.com    password
student@example.com        password
```

---

## Screenshots

![LearnForge LMS Instructor Courses Dashboard](/assets/learnforge-lms/instructor_course_dash.png)

![LearnForge LMS Instructor Lessons Dashboard](/assets/learnforge-lms/instructor_lesson_dash.png)

![LearnForgeLMS Student Lesson Viewer](/assets/learnforge-lms/student_lesson_viewer.png)
