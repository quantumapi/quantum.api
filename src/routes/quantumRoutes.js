const express = require('express');
const router = express.Router();
const { exec } = require('child_process');

// Middleware to start the FastAPI server
router.use((req, res, next) => {
  exec('uvicorn app:app --host 0.0.0.0 --port 8000', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error starting server: ${error.message}`);
      return res.status(500).send('Internal Server Error');
    }
    if (stderr) {
      console.error(`Server stderr: ${stderr}`);
      return res.status(500).send('Internal Server Error');
    }
    console.log(`Server stdout: ${stdout}`);
    next();
  });
});

// Define a simple route to test the setup
router.get('/', (req, res) => {
  res.send('Quantum API is running');
});

module.exports = router;
