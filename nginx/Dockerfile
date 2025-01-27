FROM nginx:latest

# Remove any existing config files
RUN rm /etc/nginx/conf.d/default.conf
# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d
# Expose port 80 for Nginx
EXPOSE 80