#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command-line arguments (third argument)
const apiUrl = process.argv[2];

// Make an HTTP GET request to the provided API URL
request(apiUrl, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  // Parse the response body as JSON
  const todos = JSON.parse(body);

  // Initialize an object to store the count of completed tasks by user ID
  const completedTasks = {};

  // Loop through each task (todo) in the todos array
  todos.forEach(todo => {
    // Check if the task is marked as completed
    if (todo.completed) {
      // If the user ID already exists in completedTasks, increment the count
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        // If it doesn't exist, initialize it with a count of 1
        completedTasks[todo.userId] = 1;
      }
    }
  });

  // Print the completedTasks object, which now contains counts of completed tasks by user ID
  console.log(completedTasks);
});
