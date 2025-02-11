import express, { Request, Response, NextFunction } from 'express';
import helmet from 'helmet';
import cors from 'cors';
import { config } from './config';
import logger from './logger';
import apiRouter from './api';

const app = express();

// Security middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Basic request logging
app.use((req: Request, res: Response, next: NextFunction) => {
  logger.info(`Incoming request: ${req.method} ${req.url}`);
  next();
});

// API routes
app.use('/api', apiRouter);

// Health check endpoint
app.get('/health', (req: Request, res: Response) => {
  res.status(200).json({ status: 'OK', timestamp: new Date() });
});

// Global error handler
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  logger.error(`Error: ${err.message}`);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
app.listen(config.port, () => {
  logger.info(`Quantum API is running on port ${config.port} in ${config.nodeEnv} mode.`);
});
