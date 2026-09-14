# Event Ticketing Platform - Final Project (Coding Factory 10)

Αυτή η εφαρμογή αποτελεί την τελική εργασία για το **Coding Factory 10** του **Οικονομικού Πανεπιστημίου Αθηνών (ΟΠΑ)**. Πρόκειται για μια ολοκληρωμένη πλατφόρμα διαχείρισης και 
κρατήσεων εκδηλώσεων (Event Ticketing System).

---

## Tech Stack

* **Back-end:** Python 3.11, FastAPI
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **Authentication & Authorization:** JWT (JSON Web Tokens), Passlib
* **Containerization:** Docker & Docker Compose
* **API Documentation:** Swagger UI / OpenAPI
* **Front-end:** HTML5, Tailwind CSS, JavaScript (Fetch API)

---

## Layered Architecture

Η εφαρμογή ακολουθεί αυστηρά τη διαστρωμάτωση ευθυνών:

* **Domain Models (`models/`):** Ορισμός των οντοτήτων και των σχέσεων στη βάση δεδομένων.
* **Pydantic Schemas (`schemas/`):** Data validation και serialization για τα Requests/Responses.
* **Repository Layer (`repositories/`):** Διαχείριση των queries στη Βάση Δεδομένων (CRUD).
* **Service Layer (`services/`):** Επιχειρηματική λογική (Business Logic) & validation κανόνων.
* **Controllers / Routers (`api/`):** Endpoints του REST API.

---

## Domain Model

Το μοντέλο δεδομένων αποτελείται από τις εξής οντότητες:

1. **User:** Διαχειρίζεται το Authentication/Authorization με ρόλους (`ADMIN`, `ORGANIZER`, `CUSTOMER`).
2. **Event:** Περιλαμβάνει πληροφορίες εκδήλωσης, τιμή, τοποθεσία και διαθέσιμα εισιτήρια.
3. **Booking:** Συνδέει έναν `CUSTOMER` με ένα `Event`, υπολογίζοντας αυτόματα το συνολικό κόστος.

---

## Οδηγίες Build & Deploy (με Docker)

### Προαπαιτούμενα
* Docker Desktop εγκατεστημένο.

### Βήματα Εκτέλεσης
1. Κάντε clone το repository:
   ```bash
   git clone [https://github.com/kkarmp/event-ticketing-platform.git](https://github.com/kkarmp/event-ticketing-platform.git)
   cd event-ticketing-platform
