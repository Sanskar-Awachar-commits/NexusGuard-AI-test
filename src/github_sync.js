const axios = require('axios');

// TruffleHog flags the "ghp_" prefix as a exposed Personal Access Token
const GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD";

axios.defaults.headers.common['Authorization'] = `Bearer ${GITHUB_TOKEN}`;