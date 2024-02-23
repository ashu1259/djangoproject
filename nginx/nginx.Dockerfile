# Use an official Nginx image
FROM nginx:alpine

# Copy nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to the outside world
EXPOSE 80
