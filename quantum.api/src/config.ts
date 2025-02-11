import dotenv from 'dotenv';
dotenv.config();

export const config = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || 'development',
  quantumApiKey: process.env.QUANTUM_API_KEY || 'default_api_key', // Replace with secure key management in production
  encryptionSecret: process.env.ENCRYPTION_SECRET || 'default_secret', // Must be overridden with a secure key in production
  logLevel: process.env.LOG_LEVEL || 'info'
};
