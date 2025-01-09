# Django CRUD API

This is a Django-based CRUD API for managing messages between senders and recipients. The API allows you to **Create**, **Read**, **Update**, and **Delete** messages. The project is deployed and accessible at [https://django-crud-api-ejoi.onrender.com/](https://django-crud-api-ejoi.onrender.com/).

---

## **Features**
1. Create a new message.
2. Retrieve all messages.
3. Update an existing message by ID.
4. Delete a message by ID.

---

## **Deployed URL**
The application is live and can be accessed here:
[https://django-crud-api-ejoi.onrender.com/](https://django-crud-api-ejoi.onrender.com/)

---

## **Endpoints**
### **1. Create a Message**
- **URL**: `/api/create/`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
      "sender": "Alice",
      "recipient": "Bob",
      "content": "Hello, Bob!"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Message created",
      "id": 1
  }
  ```

---

### **2. Retrieve All Messages**
- **URL**: `/api/read/`
- **Method**: `GET`
- **Response**:
  ```json
  [
      {
          "id": 1,
          "sender": "Alice",
          "recipient": "Bob",
          "content": "Hello, Bob!",
          "timestamp": "2025-01-04T10:30:00Z",
          "is_edited": false
      }
  ]
  ```

---

### **3. Update a Message**
- **URL**: `/api/update/<message_id>/`
- **Method**: `PUT`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
      "content": "Updated message content"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Message updated"
  }
  ```

---

### **4. Delete a Message**
- **URL**: `/api/delete/<message_id>/`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
      "message": "Message deleted"
  }
  ```

---

## **Testing the API**
You can test the API using tools like:
- **Postman**
- **cURL**
- Any HTTP client

Replace `<message_id>` with the actual ID of a message retrieved from the **GET** endpoint.

---

## **Technologies Used**
- **Backend**: Django 5.1.4
- **Deployment**: Render (Free Tier)
- **Dependencies**:
  - Gunicorn
  - Whitenoise

---

## **How to Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/JSK1105/django-crud-api.git
   cd django-crud-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Access the API locally at `http://127.0.0.1:8000/`.

---

## **Deployed Link**
Visit the deployed project at [https://django-crud-api-ejoi.onrender.com/](https://django-crud-api-ejoi.onrender.com/).

---
