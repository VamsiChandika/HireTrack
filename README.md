# HireTrack – Smart Job & Placement Management System

HireTrack is a full-stack Job and Placement Management System developed using Django, Django REST Framework, MySQL and Bootstrap.

The platform connects job seekers and recruiters through a centralized system where candidates can explore jobs, apply for opportunities, manage their profiles and track application statuses. Recruiters can publish job openings and manage applications, while administrators oversee users, jobs and applications.

## Features

### 1. Job Seeker
- User registration and login.
- Role-based dashboard.
- Browse and search job opportunities.
- View detailed job descriptions.
- Apply for jobs.
- Duplicate application prevention.
- Track application status.
- Manage candidate profile.
- Upload and view resumes.

### 2. Recruiter
- Recruiter registration and login.
- Recruiter dashboard with statistics.
- Create, view, edit and delete job postings.
- View applications received for posted jobs.
- Update candidate application statuses.
- Manage recruitment activities.

### 3. Administrator
- Django Admin integration.
- Manage users and user roles.
- View and manage job postings.
- Manage candidate applications.
- Update application statuses.
- View platform statistics.

### 4. Additional Features
- Role-based access control.
- Search and filtering.
- Job ordering and pagination.
- Form validation.
- Resume file management.
- Responsive design for mobile, tablet and desktop.
- Django messages and session-based authentication.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django 5.2 | Web framework |
| Django REST Framework | REST API development |
| MySQL 8.0 | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| Bootstrap 5.3 | Responsive UI |
| JavaScript | No custom frontend JavaScript required |
| VS Code | Development environment |
| MySQL Workbench | Database management |

## Project Structure

```text
HireTrack/
│
├── myenv/
│
├── backend_Hiretrack/
│   │
│   ├── accounts/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── tests.py
│   │
│   ├── jobs/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── tests.py
│   │
│   ├── applications/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── tests.py
│   │
│   ├── dashboard/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   │
│   ├── media/
│   ├── manage.py
│   └── requirements.txt
│
└── README.md
```

## API Documentation

Base URL:

```text
http://127.0.0.1:8000/
```

### 1. Accounts API

Base path: `/api/accounts/`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/accounts/register/` | Register user |
| POST | `/api/accounts/login/` | User authentication |
| POST | `/api/accounts/profile/create/` | Create candidate profile |
| GET | `/api/accounts/profile/` | Retrieve candidate profile |
| PUT | `/api/accounts/profile/` | Update candidate profile |
| PATCH | `/api/accounts/profile/` | Partially update profile |
| DELETE | `/api/accounts/profile/` | Delete candidate profile |
| PUT | `/api/accounts/profile/skills/` | Update candidate skills |
| PATCH | `/api/accounts/profile/skills/` | Partially update skills |

### 2. Jobs API

Base path: `/api/jobs/`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/jobs/` | List active jobs |
| POST | `/api/jobs/` | Create job |
| GET | `/api/jobs/<id>/` | Retrieve job details |
| PUT | `/api/jobs/<id>/` | Update job |
| PATCH | `/api/jobs/<id>/` | Partially update job |
| DELETE | `/api/jobs/<id>/` | Delete job |

**Search and filtering examples**

```text
/api/jobs/?search=Python
/api/jobs/?location=Hyderabad
/api/jobs/?job_type=FULL_TIME
/api/jobs/?experience_required=0
/api/jobs/?ordering=salary_min
/api/jobs/?ordering=-salary_min
/api/jobs/?page=1
```

Pagination is configured with a page size of 5.

### 3. Applications API

Base path: `/api/applications/`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/applications/` | Apply for a job |
| GET | `/api/applications/my/` | View own applications |
| GET | `/api/applications/recruiter/` | View recruiter applications |
| PATCH | `/api/applications/<id>/status/` | Update application status |
| PUT | `/api/applications/<id>/status/` | Update application status |

Application status values:

- `APPLIED`
- `UNDER_REVIEW`
- `SHORTLISTED`
- `REJECTED`
- `SELECTED`

Example status update:

```json
{
    "status": "SHORTLISTED"
}
```

### 4. Dashboard API

Endpoint:

```text
GET /api/dashboard/
```

Provides statistics based on the authenticated user's role.

- **Job Seeker:** Total applications and application status counts.
- **Recruiter:** Total jobs, active jobs, applications and status counts.
- **Admin:** Total users, job seekers, recruiters, jobs and application statistics.

### 5. Authentication and Admin

| Endpoint | Description |
|---|---|
| `/admin/` | Django Administration |
| `/api-auth/` | REST Framework browsable API authentication |
| `/api/accounts/login/` | API token login |

Token-authenticated API requests use:

```http
Authorization: Token YOUR_TOKEN
```

The frontend uses Django authentication and sessions.

## Installation and Setup

### Prerequisites

- Python 3.12 or later
- MySQL Server
- MySQL Workbench
- Visual Studio Code

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd HireTrack
```

Replace the repository URL with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv myenv
```

Activate it on Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

Navigate into the Django project:

```bash
cd backend_Hiretrack
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL

Create a MySQL database:

```sql
CREATE DATABASE hiretrack_db;
```

Configure the database connection in Django settings using your local database credentials.

Keep database passwords and Django secret keys outside public source control.

### Step 5: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Admin Account

```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## Automated Testing

The project includes Django automated tests for its main applications.

Run all tests:

```bash
python manage.py test
```

Current test results:

| Application | Tests |
|---|---:|
| Accounts | 1 |
| Jobs | 1 |
| Applications | 2 |
| Dashboard | 4 |
| **Total** | **8 passed** |

Additional project checks:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py showmigrations
```

All 8 automated tests passed during project verification.

## Current Project Status

- Backend development completed.
- MySQL database integration completed.
- REST API development completed.
- Frontend development completed.
- Job Seeker workflow tested.
- Recruiter workflow tested.
- Admin workflow tested.
- Role-based access tested.
- Application status synchronization tested.
- Responsive design tested.
- Automated testing completed with 8 passing tests.
- README documentation updated.

## Future Enhancements

- Deployment to a production server.
- GitHub repository setup and maintenance.
- Production security configuration.
- Additional automated API and integration tests.
- Email notifications for application status updates.

## Security Notes

- Never upload passwords, database credentials, API tokens or Django secret keys to GitHub.
- Use environment variables for sensitive configuration.
- Configure `DEBUG=False`, allowed hosts and secure cookies before production deployment.
- Configure secure media storage for production resume uploads.

## Author

Developed as a Python Full Stack project using Django, Django REST Framework, MySQL and Bootstrap.
