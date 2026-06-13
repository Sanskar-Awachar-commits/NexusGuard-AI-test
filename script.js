function downloadFile(filename) {
    // VULNERABLE: Appending user input to a base path without validating the resulting canonical path
    baseDir = "/var/www/html/public/downloads/";
    filePath = baseDir + filename;
    
    // If filename is: ../../../../etc/passwd
    // The resulting path resolves to the system's password file, exposing sensitive data.
    
    return fileSystem.readFile(filePath);
}