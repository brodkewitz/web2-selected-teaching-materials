---
date-created: 2021-12-09
date-updated: [2021-10-03]
tags: [assignment, web2]
title: "Assignment: Animation in the Browser"
points: 60
---

# Assignment: Animation in the Browser

Create a scroll triggered animation using svg shapes and the Greensock javascript library. Pad the top of your html document so that the shapes are below the initial viewport (e.g. set the container `margin-top: 100vh`, or similar). The animation should play when scrolled into view, not on initial page load.

You can create and animate anything you want! The animation(s) can be subtle or wild, though I encourage you to aim for fun, tasteful, effective, refined, rather than pure Chaotic Evil. (Maybe don't flip our stomachs or make something that requires a seizure warning. 😵)

When planning an animation, it's really helpful to sketch out both a mockup of the scene and the animation steps, before exporting assets and reconstructing it in the browser. The sketches can even be on paper—they're just to help you visualize and think through how everything will work.

Don't try to bite off more than you can chew on this assignment! All of the steps for this assignment take time, and it may be easy to plan a complicated animation and not allot enough time for everything else. All of these steps will take some time: sketching ideas, drawing your vector assets, organizing them in the layers palette, exporting and setting up the html and css layout, and finally the javascript.


## Purpose

- Practice preparing and exporting SVG
- Practice embedding SVG content into an HTML layout
- Learn the basics of Greensock and some of its animation features


## Project Components

1. **Planning materials.** Sketch, diagram, or otherwise storyboard the steps of your animation. Do this even if the animation(s) are simple. Don't worry about polish - crayons and stick figures welcome. The point is to help you think through specifically what needs to change and how for the animation to work.

1. **Offline assets.** Include the Illustrator/Sketch/original vector files with organized shapes and named layers. Also include the exported SVG file that you ultimately embed in your html.

1. **Complete single page site.** There are two ways you can set this up, depending on your preference:

    One way is to embed everything in the html. The svg of course, your css between `<style>` tags in the `<head>`, and your javascript in `<script>` tags at the bottom of the `<body>`. This keeps everything in one file which is simple for very small projects like this.

    The other option is to link to separate css and/or js files as usual, like with a bigger project. The advantage here is you can use VSCode's split panes and see more code on screen at once.


## Submission Instructions

This project should be submitted in two ways:

1. Deployed to web2.immtcnj.com under your named directory. Only upload the website itself, not the offline assets. The site should fully function in a browser but nothing will be collected or downloaded from here.

2. Uploaded to the Shared Google Drive. This is where to upload the full project folder, including offline assets like your sketches and Illustrator file.

Here's an example of how to organize your project directory:

```
animation-in-the-browser/
├── assets/
│   ├── animation-mockup-sketch-01.jpg
│   ├── animation-mockup-sketch-02.jpg
│   ├── animation-mockup-sketch-03.jpg
│   ├── animation-exported.svg
│   └── animation.ai
└── animation-in-the-browser/
    └── index.html
```
