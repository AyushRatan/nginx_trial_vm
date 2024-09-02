# Dockerfile for React App
FROM node:20 AS build

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source files
COPY . .

# Build the React app
RUN npm run build

# Use a lightweight image to serve the built files
FROM nginx:alpine

# Copy the built React app to the Nginx web root
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80