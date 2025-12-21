# LearnForge LMS

## Summary

A Learning Management System built as a full-stack Rails app with Hotwire interactivity, TDD, and role-based access. Demonstrates clean architecture and dynamic UIs. Designed for instructors and learners, with role-based access and lesson progress tracking.

[View the code](https://github.com/ajtran303/learnforge-lms/)

---

## Highlights

- **Role-based access:** Learner & Instructor roles with proper authorization
- **Course & Lesson Management:** Create, edit, and track lessons and courses
- **Interactive UI:** Turbo-powered updates, inline editing, and progress bars
- **Test-Driven Development:** RSpec & Capybara for models, views, and integration

---

## Tech Stack

- Ruby on Rails 8.1
- PostgreSQL
- Turbo & Bootstrap 5
- Authentication with `bcrypt`
- Deployment: Render

---

## Demo

- **Live Demo:** ([Requires login](https://learnforge-lms.onrender.com))
<!-- - **Demo Video:** [Watch on YouTube]() *(TODO: Record demo)* -->

---

## Screenshots

![LearnForge LMS Instructor Courses Dashboard](https://private-user-images.githubusercontent.com/31839316/528914119-85e72ca0-bedc-4991-b66c-6d35ea49f248.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzY2NDEsIm5iZiI6MTc2NjI3NjM0MSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTQxMTktODVlNzJjYTAtYmVkYy00OTkxLWI2NmMtNmQzNWVhNDlmMjQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwMTkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYxOTc5YThlY2I5Mjk5NmM0ZjI0NzRjNmRmZjg2MGE1MjA3MDdmNDE2ZmJiNWRmMjZlZDdhM2NlODM3NmU4NzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.EBJqgO7S6tSUjQFOLBdAKE-NwnuVuV6TUcJEcgRY5jk)

![LearnForge LMS Instructor Lessons Dashboard](https://private-user-images.githubusercontent.com/31839316/528914121-fbf4c9ef-99a4-4266-967c-8fa749e66153.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzY2NDEsIm5iZiI6MTc2NjI3NjM0MSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTQxMjEtZmJmNGM5ZWYtOTlhNC00MjY2LTk2N2MtOGZhNzQ5ZTY2MTUzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwMTkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZjYmE0N2I3YjJmMGJiYzMzYTg4M2ZlZTNlZjhmNzVlN2YzMGZiM2JlZDc5NTE5NzFjNTc5N2YzNjg0YzcyMTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.VOjlLzDpd0ZnKfx6VmpPEa5vlMi3nOFqBFF3qk_aT5w)

![LearnForgeLMS Student Lesson Viewer](https://private-user-images.githubusercontent.com/31839316/528914123-a366a470-0caa-47c3-8d3e-1f0cc19b2717.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjYyNzY2NDEsIm5iZiI6MTc2NjI3NjM0MSwicGF0aCI6Ii8zMTgzOTMxNi81Mjg5MTQxMjMtYTM2NmE0NzAtMGNhYS00N2MzLThkM2UtMWYwY2MxOWIyNzE3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjIxVDAwMTkwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBlYTVlMWViOTUzYWM1YzE1NzA1ZDhkNzhmNDBlOTdhM2QzNzA5NTg2NTYxMTg3ODRjZTE0MzU2MDJhNzM1OWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.VlruQhqv1-wCHszNxCPwCdoJB3_zsqLwpaJG-4UK0hw)