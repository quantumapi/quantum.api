const { exec } = require('child_process');

// Function to set up logging using Python's logging module
const setupLogging = () => {
  exec('python -c "from utils import setup_logging; setup_logging()"', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error setting up logging: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Logging setup stderr: ${stderr}`);
      return;
    }
    console.log(`Logging setup stdout: ${stdout}`);
  });
};

setupLogging();
