// BAD: Using unsafe C-style string functions
void processInput(const char* userInput) {
    char buffer[64];
    
    // If userInput is longer than 63 characters (plus the null terminator),
    // it will overwrite memory outside 'buffer'.
    strcpy(buffer, userInput); 
    
    printf("Processing: %s\n", buffer);
}