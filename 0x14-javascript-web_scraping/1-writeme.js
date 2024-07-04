#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Get the file name and content from command line arguments
const file = process.argv[2];
const content = process.argv[3];

try {
  // Write the content to the specified file with 'utf-8' encoding
  fs.writeFileSync(file, content, 'utf-8');
} catch (err) {
  // Log any errors that occur during the write process
  console.error(err);
}
