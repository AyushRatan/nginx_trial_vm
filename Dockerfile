
# Use the official Nginx image as a base
FROM nginx:alpine

# Copy custom nginx.conf to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy self-signed SSL certificates into the container
COPY ./ssl/certs/fullchain.pem /etc/ssl/certs/fullchain.pem
COPY ./ssl/certs/privkey.pem /etc/ssl/certs/privkey.pem

# Copy DH parameters if you are using them for SSL
# # If you're not using DH parameters, you can skip this line
# COPY /path/to/ssl/certs/dhparam.pem /etc/ssl/certs/dhparam.pem

# Copy the static files into Nginx
COPY ./dist /usr/share/nginx/html

# Expose ports 80 (HTTP) and 443 (HTTPS)
EXPOSE 80
EXPOSE 443