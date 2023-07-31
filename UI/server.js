const express = require("express");
const app = express();
const port = 9000; // The port number you want to use

app.use(express.static("public")); // Assuming your HTML, CSS, and JavaScript files are in a 'public' folder

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
