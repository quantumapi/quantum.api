const { exec } = require('child_process');

// Function to start the FastAPI server
const startServer = () => {
  exec('uvicorn app:app --host 0.0.0.0 --port 8000', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error starting server: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Server stderr: ${stderr}`);
      return;
    }
    console.log(`Server stdout: ${stdout}`);
  });
};

module.exports = {
  startServer
};
