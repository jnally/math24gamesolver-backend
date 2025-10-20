const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.post('/api/calculate', (req, res) => {
    const { num1, num2, num3, num4 } = req.body;

    if ([num1, num2, num3, num4].some(n => n === undefined || isNaN(n))) {
        return res.status(400).json({ message: 'All four inputs must be valid positive integer numbers.' });
    }
    
    const pythonProcess = spawn('python', [
        'math24solver.py',
        String(num1),
        String(num2),
        String(num3),
        String(num4)
    ]);

    let dataString = '';
    let errorString = '';

    pythonProcess.stdout.on('data', (data) => {
        dataString += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        errorString += data.toString();
        console.error(`Python stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
        
        if (code !== 0) {
            return res.status(500).json({ message: 'Failed to run Python script.', error: errorString });
        }
        
        try {
            const result = JSON.parse(dataString);
            res.json({ results: result });
        } catch (e) {
            console.error('Error parsing JSON from Python script:', e);
            res.status(500).json({ message: 'Invalid output from Python script.' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
