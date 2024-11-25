# Use the MySQL 8.0.40 Debian-based image
FROM mysql:8.0.40-debian

# Set environment variables for MySQL user, password, root password, and database
ENV MYSQL_USER=yahya
ENV MYSQL_PASSWORD=yahya
ENV MYSQL_ROOT_PASSWORD=yahya
ENV MYSQL_DATABASE=users

# Update and install additional tools
RUN apt-get update &&     apt-get install -y net-tools iputils-ping nano &&     rm -rf /var/lib/apt/lists/*

# Copy the custom my.cnf file to override the default MySQL configuration
COPY my.cnf /etc/mysql/my.cnf

# Expose the default MySQL port
EXPOSE 3306
