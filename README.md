# 📚 Library - Bookstore E-commerce

> A minimalist yet powerful Django e-commerce platform built for small bookshops looking to establish an online presence.

![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue)
![Django Version](https://img.shields.io/badge/Django-3.1.4-green)
![Deployment](https://img.shields.io/badge/Deployed-Heroku-purple?logo=heroku)

![Screenshot](/media/home.jpg)

**Live Demo**: [https://salvo-library.herokuapp.com/](https://salvo-library.herokuapp.com/)

---

## 🚀 Features

- **User Authentication**: Secure registration, login, and password recovery
- **Responsive Design**: Mobile-first approach for seamless browsing across all devices
- **Product Management**: Admin can add, edit, and delete books with all relevant details
- **Advanced Sorting**: Sort books by price, rating, name, or category
- **Category Navigation**: Filter books by genre or special offers
- **Shopping Cart**: Add, adjust quantity, or remove items before checkout
- **Secure Payments**: Integrated with Stripe for secure transaction processing
- **User Profiles**: View purchase history and save delivery information
- **Search Functionality**: Quickly find books with the intuitive search bar
- **Order Confirmation**: Email notifications for successful purchases

---

## 🛠️ Tech Stack

| Layer       | Technologies                                |
|-------------|---------------------------------------------|
| **Backend** | Django 3.1.4                                |
| **Frontend**| HTML5, CSS3, JavaScript, Bootstrap 4.4      |
| **Database**| PostgreSQL (production), SQLite (development)|
| **Auth**    | Django Allauth                              |
| **Payment** | Stripe                                      |
| **Cloud**   | AWS S3 (media & static files)               |
| **Deployment** | Heroku                                   |

---

## 📦 Installation & Setup

```bash
git clone https://github.com/yourusername/library.git
cd library
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 🔐 Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_db_url
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
EMAIL_HOST_USER=your_email_address
EMAIL_HOST_PASS=your_email_app_password
```

---

## 🔄 Migrations & Seed Data

```bash
python manage.py migrate
python manage.py loaddata categories
```

---

## 👤 User Roles & Credentials

| Role   | Access                              |
|--------|-------------------------------------|
| Admin  | Full site management, product CRUD  |
| User   | Browsing, purchasing, profile management |

For testing purposes:
- Admin: admin@library.com / testpassword123
- User: user@library.com / testpassword123

---

## 📁 Project Structure

```
library/
├── bag/                    # Shopping bag functionality
├── checkout/               # Checkout and payment processing
├── home/                   # Home page app
├── library/                # Main project settings
├── media/                  # Product images
├── products/               # Product management
├── profiles/               # User profile management
├── static/                 # Static files (CSS, JS)
├── templates/              # HTML templates
│   ├── allauth/            # Authentication templates
│   └── includes/           # Reusable template components
├── .gitignore              # Git ignore file
├── Procfile                # Heroku deployment configuration
├── README.md               # Project documentation
├── manage.py               # Django project management
└── requirements.txt        # Python dependencies
```

---

## 🧪 Testing

Tested on:

- ✅ Desktop: Chrome, Firefox, Safari
- ✅ Mobile: Android Chrome, iOS Safari
- ✅ Tablet: iPad Safari, Android Chrome
- ✅ Payment Processing: Stripe test cards

The following test tools were used:
- HTML validator - W3C
- CSS validator - Jigsaw
- JavaScript validation - JSHint
- Python validation - PEP8
- Lighthouse - Performance testing

---

## 🌍 Deployment

### Local Deployment

1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`
3. Set up environment variables
4. Run migrations with `python manage.py migrate`
5. Start the server with `python manage.py runserver`

### Heroku Deployment

1. Create a Heroku app
2. Connect your GitHub repository
3. Add required config vars (see environment variables)
4. Enable Heroku Postgres
5. Deploy the main branch

---

## 🔮 Future Enhancements

- Customer reviews and ratings
- Book recommendation system
- Wishlist functionality
- Advanced search filters
- Author spotlights and book collections
- Newsletter subscription
- Multiple payment options
- Book preview functionality
- Mobile app version

---

## 🙏 Credits

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/)
- Product images and descriptions adapted from various bookstore websites for educational purposes
- [Code Institute](https://codeinstitute.net/) for project guidance

---

## 📜 License

This project is licensed under the MIT License

---

## 👨‍💻 Author

**Salvatore Bevilacqua**  
