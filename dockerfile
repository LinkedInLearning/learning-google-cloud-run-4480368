FROM nginx:latest
COPY index.html  /usr/share/nginx/html
COPY forestbridge.jpg /usr/share/nginx/html