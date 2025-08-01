# IT Solutions Static Page Demo

This repository contains a static HTML page for an IT consulting services company, designed with a modern UI using Tailwind CSS.

## Project Overview

This is a simple static website for an IT consulting company that showcases:
- Services offered
- About the company
- Testimonials
- Contact information

The page is fully responsive and features a clean, professional design.

## Technologies Used

- HTML5
- [Tailwind CSS](https://tailwindcss.com/) (via CDN)
- JavaScript (minimal, for mobile menu toggle)
- PHP (for serving the static content)

## Project Structure

```
demo-static-page/
├── .dockerignore       # Files to exclude from Docker builds
├── Dockerfile          # Docker configuration for PHP server
├── compose.yaml        # Docker Compose configuration
├── index.html          # Main static HTML page
└── src/                # Source directory (empty, for future development)
```

## Running Locally

### Using PHP's Built-in Server

If you have PHP installed locally, you can run:

```bash
php -S localhost:8000
```

Then visit `http://localhost:8000` in your browser.

### Using Docker

Build and run using Docker:

```bash
# Build the Docker image
docker build -t it-solutions-static .

# Run the container
docker run -p 8000:8000 it-solutions-static
```

Or using Docker Compose:

```bash
docker-compose up
```

Then visit `http://localhost:8080` in your browser.

## Development

This is a simple static page that can be modified directly by editing the HTML file. The page uses Tailwind CSS via CDN, so no build process is required for styling changes.

## License

This project is available for educational purposes.

## Author

Created as part of the YouTube videos code examples series.
