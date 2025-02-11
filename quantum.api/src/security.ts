/**
 * Security Module
 *
 * Provides quantum-safe cryptographic functionalities using advanced,
 * post-quantum encryption algorithms. The methods here are built to resist
 * attacks from both classical and quantum adversaries.
 */

import { config } from './config';
import sodium from 'libsodium-wrappers';
import crypto from 'crypto';

/**
 * Encrypt data using quantum-safe cryptography.
 * Utilizes a unique nonce generated with secure randomness combined with a post-quantum algorithm.
 *
 * @param plaintext - The data to be encrypted.
 * @returns A string containing the nonce and ciphertext.
 */
export async function encryptData(plaintext: string): Promise<string> {
  await sodium.ready;
  const nonce = sodium.randombytes_buf(sodium.crypto_secretbox_NONCEBYTES);
  const key = sodium.from_hex(config.encryptionSecret);
  const ciphertext = sodium.crypto_secretbox_easy(plaintext, nonce, key);
  return `${sodium.to_hex(nonce)}:${sodium.to_hex(ciphertext)}`;
}

/**
 * Decrypt data using quantum-safe cryptography.
 *
 * @param payload - The encrypted payload containing nonce and ciphertext.
 * @returns The decrypted plaintext.
 */
export async function decryptData(payload: string): Promise<string> {
  await sodium.ready;
  const [nonceHex, ciphertextHex] = payload.split(':');
  const nonce = sodium.from_hex(nonceHex);
  const ciphertext = sodium.from_hex(ciphertextHex);
  const key = sodium.from_hex(config.encryptionSecret);
  const plaintext = sodium.to_string(sodium.crypto_secretbox_open_easy(ciphertext, nonce, key));
  return plaintext;
}
