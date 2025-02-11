# Use Node.js LTS version as the base image
FROM node:18-alpine

# Create and set the working directory
WORKDIR /usr/src/app

# Copy dependency definitions and install production dependencies
COPY package*.json ./
RUN npm install --only=production

# Bundle the application source code
COPY . .

# Build the TypeScript code
RUN npm run build

# Expose the application port (ensure it matches the config)
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]
