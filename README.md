# Quickoo Car Service Website

A production-ready car service provider website built with Flask, featuring a modern, responsive design and comprehensive functionality for a UK-based luxury transportation company.

## Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI/UX**: Clean, professional design with smooth animations
- **SEO Optimized**: Meta tags, semantic HTML, and optimized content
- **Contact Form**: Functional contact form with validation
- **Legal Pages**: UK-compliant Privacy Policy and Terms & Conditions
- **Performance Optimized**: Fast loading times with optimized assets
- **Accessibility**: WCAG compliant with proper contrast and semantic markup

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Templating**: Jinja2
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/quickoo-car-service.git
cd quickoo-car-service
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Run the application:
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`

## Project Structure

```
quickoo-car-service/
│
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── run.py                # Application runner
├── requirements.txt      # Python dependencies
│
├── static/
│   ├── css/
│   │   ├── style.css    # Main stylesheet
│   │   └── responsive.css # Responsive styles
│   └── js/
│       └── main.js      # JavaScript functionality
│
├── templates/
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   ├── contact.html     # Contact page
│   ├── privacy.html     # Privacy Policy
│   ├── terms.html       # Terms & Conditions
│   └── 404.html         # Error page
│
└── utils/               # Utility modules
    └── __init__.py
```

## Deployment

### Production Deployment with Gunicorn

1. Install Gunicorn (included in requirements.txt)

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Environment Variables

Set these environment variables for production:

- `SECRET_KEY`: Strong secret key for session management
- `FLASK_ENV`: Set to 'production'
- `DEBUG`: Set to 'False'
- `MAIL_SERVER`: SMTP server for emails
- `MAIL_USERNAME`: Email account username
- `MAIL_PASSWORD`: Email account password

### Nginx Configuration (Example)

```nginx
server {
    listen 80;
    server_name quickoo.co.uk www.quickoo.co.uk;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/quickoo-car-service/static;
        expires 30d;
    }
}
```

## Customization

### Branding
- Logo: Update logo URL in `base.html`
- Colors: Modify CSS variables in `style.css`
- Company Info: Update details in `config.py`

### Content
- Service descriptions in `index.html`
- Company story in `about.html`
- Legal content in `privacy.html` and `terms.html`

### Functionality
- Add email functionality by configuring SMTP in `config.py`
- Implement booking system by extending the Flask routes
- Add payment integration (Stripe, PayPal, etc.)
- Implement user authentication for account management

## Security Considerations

- Always use HTTPS in production
- Keep SECRET_KEY secure and unique
- Regularly update dependencies
- Implement rate limiting for forms
- Add CSRF protection (Flask-WTF)
- Sanitize all user inputs

## Performance Optimization

1. **Enable Caching**:
   - Static file caching via Nginx
   - Browser caching headers
   - CDN for static assets

2. **Minify Assets**:
   - CSS and JavaScript minification
   - Image optimization
   - Lazy loading for images

3. **Database Optimization** (when implemented):
   - Query optimization
   - Connection pooling
   - Caching frequently accessed data

## SEO Best Practices

- Semantic HTML structure
- Meta descriptions on all pages
- Structured data markup
- XML sitemap
- Robots.txt file
- Page speed optimization
- Mobile-responsive design

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Android)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is proprietary to Quickoo PVT LTD. All rights reserved.

## Support

For support, email support@quickoo.co.uk or call +44 20 1234 5678.

## Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for icons
- Unsplash for high-quality images
- Flask community for excellent documentation