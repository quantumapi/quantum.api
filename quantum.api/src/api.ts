import { Router, Request, Response } from 'express';
import { quantumRandom, entangleStates } from './quantum';
import { encryptData, decryptData } from './security';
import logger from './logger';

const router = Router();

/**
 * GET /api/random
 * Returns a quantum-enhanced random number.
 */
router.get('/random', async (req: Request, res: Response) => {
  try {
    const randomValue = quantumRandom();
    res.status(200).json({ random: randomValue });
  } catch (error) {
    logger.error(`Quantum random generation error: ${error}`);
    res.status(500).json({ error: 'Failed to generate quantum random number.' });
  }
});

/**
 * GET /api/entangle
 * Expects query parameters: stateA and stateB.
 * Returns an entangled state based on the provided states.
 */
router.get('/entangle', async (req: Request, res: Response) => {
  try {
    const stateA = parseFloat(req.query.stateA as string);
    const stateB = parseFloat(req.query.stateB as string);
    if (isNaN(stateA) || isNaN(stateB)) {
      return res.status(400).json({ error: 'Invalid state values provided.' });
    }
    const entangledState = entangleStates(stateA, stateB);
    res.status(200).json({ entangledState });
  } catch (error) {
    logger.error(`Entanglement error: ${error}`);
    res.status(500).json({ error: 'Failed to entangle states.' });
  }
});

/**
 * POST /api/encrypt
 * Expects a JSON body with a 'data' property.
 * Returns the quantum-safe encrypted version of the provided data.
 */
router.post('/encrypt', async (req: Request, res: Response) => {
  try {
    const { data } = req.body;
    if (!data) {
      return res.status(400).json({ error: 'No data provided for encryption.' });
    }
    const encrypted = await encryptData(data);
    res.status(200).json({ encrypted });
  } catch (error) {
    logger.error(`Encryption error: ${error}`);
    res.status(500).json({ error: 'Encryption failed.' });
  }
});

/**
 * POST /api/decrypt
 * Expects a JSON body with a 'payload' property.
 * Returns the decrypted plaintext from the provided payload.
 */
router.post('/decrypt', async (req: Request, res: Response) => {
  try {
    const { payload } = req.body;
    if (!payload) {
      return res.status(400).json({ error: 'No payload provided for decryption.' });
    }
    const decrypted = await decryptData(payload);
    res.status(200).json({ decrypted });
  } catch (error) {
    logger.error(`Decryption error: ${error}`);
    res.status(500).json({ error: 'Decryption failed.' });
  }
});

export default router;
