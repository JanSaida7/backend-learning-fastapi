# 🚀 Backend Engineering Journey (Python & FastAPI)

This repository documents my 12-week journey to mastering Backend Engineering, focusing on **Python**, **FastAPI**, and **PostgreSQL**.

I am following a structured roadmap to move from Python Basics to deploying a full E-Commerce Microservice.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Tools:** Docker, Git, Pytest

## 📅 Roadmap & Progress

### Phase 1: The Foundation (Weeks 1-2)
- [x] **Day 1:** Environment Setup & Type Hinting
- [x] **Day 2:** Modules, Imports & Entry Points
- [x] **Day 3:** OOP Mastery (Bank System Logic)
- [ ] **Day 4:** Decorators & Functional Patterns
- [ ] **Day 5:** JSON, Requests & API Basics
- [ ] **Week 1 Project:** CLI Weather App
- [ ] **Week 2:** Database Design (PostgreSQL)

### Phase 2: API Development (Weeks 3-5)
- [ ] **Week 3:** FastAPI Basics (Routes & Validation)
- [ ] **Week 4:** CRUD Operations (In-Memory)
- [ ] **Week 5:** Connecting Database (ORM)

### Phase 3: Professional Skills (Weeks 6-8)
- [ ] **Week 6:** Authentication (JWT)
- [ ] **Week 7:** Testing & CI/CD
- [ ] **Week 8:** Docker & Containerization

---

## 📂 Daily Log


### Day 1: Professional Setup
Set up the dev environment with Virtual Environments (`venv`) and enforced Type Hinting (`mypy`) for code quality.

### Day 2: Modules & Organization
Refactored code into modules (`math_utils.py`) to understand project structure and imports.

### Day 3: Object-Oriented Programming
Built a banking system simulation to understand **Encapsulation** and **Inheritance**.
- Created `BankAccount` class with private transaction logging.
- Implemented `SavingsAccount` inheriting from base class.
- Practiced protecting data using validation logic.

### Day 4: Decorators & Functional Patterns
Explored Python's "Magic" syntax to understand how frameworks like FastAPI wrap code.
- Implemented **Manual Decorators** to understand how functions wrap other functions.
- Refactored code to use the **`@syntax`** (Syntactic Sugar).
- Built practical utilities: an **Execution Timer** for performance and an **Auth Check** for simulated security.

### Day 5: JSON & APIs
Learned how to communicate with external servers using the **Requests** library.
- Fetched data using **GET** requests and parsed **JSON** responses.
- Used **Query Parameters** to filter data server-side.
- Sent data to a server using **POST** requests.

### Day 6: Database Setup & Basic SQL
Transitioned from storing data in memory to persistent storage using **PostgreSQL**.
- Created a `users` table with auto-incrementing IDs (`SERIAL`) and default timestamps.
- Practiced **CRUD** operations using raw SQL:
  - **Create:** `INSERT INTO` to add new users.
  - **Read:** `SELECT * FROM` to view data.
  - **Update/Delete:** Modifying records based on conditions (`WHERE`).


### Day 7: Relational Databases
Learned how to link tables using **Foreign Keys**.
- Created a One-to-Many relationship between `Users` and `Posts`.
- Used **INNER JOIN** to fetch combined data (Users who posted).
- Used **LEFT JOIN** to find users with no activity.

## 🏃 How to Run
1. Clone the repo:
   ```bash
   git clone [https://github.com/YourUsername/backend-learning-fastapi.git](https://github.com/YourUsername/backend-learning-fastapi.git)