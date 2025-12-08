# Blue Ink House – Author & Book Management Platform (Django)

A lightweight **Author & Book Management Platform** built using **Django**, based on the SDE Intern Assignment by **Blue Ink House**.  
This application allows you to:

- Create and approve authors  
- Add books only for approved authors  
- List authors with number of books  
- List and search books by title, genre, or author  
- Upload and display profile images and book cover images  

---

## 🚀 Features

### Author Management
- Create authors with:
  - Name  
  - Email  
  - Bio  
  - Profile Image (file upload)  
- Default status: `pending`
- Approve authors (change status from `pending` → `approved`)
- List all authors with:
  - Name  
  - Email  
  - Status  
  - Number of books  
  - Profile image thumbnail  

### Book Management
- Add books with:
  - Title  
  - Description  
  - Genre  
  - Cover Image (file upload)  
  - Author (only approved authors listed)
- List all books with:
  - Title  
  - Author  
  - Genre  
  - Short description  
  - Cover image thumbnail  

### Search
- Search books by:
  - Title  
  - Genre  
  - Author name  

### Tech Stack
- Backend: **Django**
- Frontend: **Django Templates + Bootstrap**
- Database: **SQLite (default Django DB)**
- Media Handling: **ImageField + local media storage**

---

## 🗂 Project Structure (Important Parts)

```text
blueinkhouse_project/
├─ blueinkhouse/           # Django project (settings, urls)
├─ authors/                # Author app
│   ├─ models.py
│   ├─ views.py
│   ├─ forms.py
│   ├─ urls.py
├─ books/                  # Book app
│   ├─ models.py
│   ├─ views.py
│   ├─ forms.py
│   ├─ urls.py
├─ templates/
│   ├─ base.html
│   ├─ authors/
│   │   ├─ add_author.html
│   │   └─ author_list.html
│   └─ books/
│       ├─ add_book.html
│       └─ book_list.html
├─ media/                  # Uploaded images (created at runtime)
├─ manage.py
└─ requirements.txt


🔹 Windows (Command Prompt / PyCharm Terminal)
# Create venv (if needed)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver

🔹 macOS / Linux (Terminal / PyCharm Terminal)
# Create venv (if needed)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
