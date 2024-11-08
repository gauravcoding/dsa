# Use the official NGINX image from the Docker Hub
FROM nginx:alpine

# Copy custom NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf_1

copy . .
# Copy static files to the NGINX directory

#COPY html /usr/share/nginx/html

# Expose port 80
EXPOSE 80