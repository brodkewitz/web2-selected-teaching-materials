# Web 2 Lesson/Demo: Dynamic Websites

© Brandon Rodkewitz. All rights reserved.  
This repository is provided for reference only. No license is granted to copy, modify, or distribute the contents.


## Notes

This demo involves running a simple Flask app, split into two parts. The app is a single page using a single template, including data from a plaintext list of names.

The application runs on my laptop and is exposed using ngrok for the students to access. I can show the datastore, code, and running dev server all at once on the projector.

The first portion is demoed in the browser. Students load the page with a query parameter that changes the page's output.

The second portion exposes a simple but complete RESTful API that is demoed using an HTTP dev client, like Thunder Client in VSCode. Students construct simple requests using native HTTP methods and json to perform CRUD operations on the names list.


- `lecture/Dymamic Websites.md` - Renders to html for upload to Canvas LMS

- `lecture/dynamic-websites-slides.pdf` - Keynote export for student reference after the lecture

- `demo/names.py` - Demo application
