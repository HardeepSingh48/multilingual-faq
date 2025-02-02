# Multilingual FAQ Backend

A Django-based backend application that provides multilingual FAQ support with caching and an admin panel.

## Features
- Create, update, and delete FAQs with multilingual support.
- API endpoints for retrieving FAQs in different languages.
- Redis caching for optimized performance.
- Django Admin panel for easy management.

## Installation

### **1. Clone the repository**
```sh
git clone https://github.com/your-username/multilingual-faq.git
cd multilingual-faq
```

### **2. Create a virtual environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install dependencies**
```sh
pip install -r requirements.txt
```

### **4. Apply migrations**
```sh
python manage.py migrate
```

### **5. Create a superuser**
```sh
python manage.py createsuperuser
```

### **6. Run the server**
```sh
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/api/faqs/` | Retrieve all FAQs |
| `POST` | `/api/faqs/` | Create a new FAQ |
| `GET`  | `/api/faqs/?lang=fr` | Get FAQs in French |
| `PUT`  | `/api/faqs/{id}/` | Update an FAQ |
| `DELETE` | `/api/faqs/{id}/` | Delete an FAQ |

## Contribution Guidelines
- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -m "feat: Add new feature"`).
- Push to the branch (`git push origin feature-name`).
- Open a Pull Request.

## Git & Version Control

### **Using Git for Version Control**

#### **1. Initialize Git**
```sh
git init
```

#### **2. Add a `.gitignore` File**
Create a `.gitignore` file and add:
```
venv/
__pycache__/
db.sqlite3
.env
```

#### **3. Commit Your Changes**
```sh
git add .
git commit -m "feat: Initial commit with Django setup"
```

#### **4. Push to GitHub**
1. Create a repository on GitHub.
2. Run:
```sh
git remote add origin https://github.com/your-username/multilingual-faq.git
git branch -M main
git push -u origin main
```

#### **5. Follow Conventional Commits**
```sh
git commit -m "feat: Add multilingual FAQ model"
git commit -m "fix: Improve translation caching"
git commit -m "docs: Update README with API examples"
```

## Deployment & Docker Support (Bonus)

### **1. Create a `Dockerfile`**
In the root of your project, create a **`Dockerfile`**:

```dockerfile
# Use Python base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations
RUN python manage.py migrate

# Expose the default Django port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **2. Create `docker-compose.yml`**
To manage dependencies like PostgreSQL and Redis, create a `docker-compose.yml`:

```yaml
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - redis
    environment:
      - DEBUG=True

  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
```

### **3. Build and Run Docker**
```sh
docker-compose up --build
```

### **4. Deploy to Heroku (Alternative)**
1. Install the Heroku CLI.
2. Login:  
   ```sh
   heroku login
   ```
3. Create a Heroku app:  
   ```sh
   heroku create multilingual-faq
   ```
4. Deploy:
   ```sh
   git push heroku main
   heroku run python manage.py migrate
   heroku open
   ```

## License
This project is licensed under the MIT License.

