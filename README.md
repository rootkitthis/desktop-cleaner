# desktop-cleaner

This code moves files from a source folder to different destination folders based on their file types. Here's how it works:

- The shutil and glob modules are imported.
- The src, screenshot, png, and documents variables are set to the paths of the source folder and the destination folders for screenshots, PNG images, and documents, respectively.
- The ss, pg, doc, and doc2 variables are set to patterns that will match all files in the source folder that are screenshots, PNG images, PDF documents, or Word documents, respectively.
- Three functions, mv_screenshot(), mv_png(), and mv_docs(), are defined to move the files to their respective destination folders.
- Each function uses a for loop with glob.iglob() to loop through all files that match the corresponding pattern, and calls shutil.move() to move each file to its respective destination folder.
- The functions are called using print() statements to move the files.

Overall, this code is a simple and efficient way to move files of different types from a source folder to their respective destination folders.
