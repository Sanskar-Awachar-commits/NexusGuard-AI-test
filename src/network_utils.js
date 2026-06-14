const { exec } = require('child_process');

function runPing(targetIp) {
    // Semgrep flags this: un-sanitized variable passed directly to the shell
    exec('ping -c 4 ' + targetIp, (err, stdout, stderr) => {
        console.log(stdout);
    });
}