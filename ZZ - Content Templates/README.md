# Intro
Use this template to update course material and to maintain consistent styling.  It is here as a guide.  That is, mostly follow the guide, but deviate from the guide when appropriate.

# General Structure
The file structure for the repo is as below:

`topic -> lesson name -> lesson material`

For example, there is a `Python` folder that has multiple lessons as subfolders.  Inside of those subfolders are the lesson materials.  

For any given lesson, it should ideally have the following content:

- Readme (short lesson summary with reference material)
- Lesson slides
- Practical Exercise instructions
- Practical Exercise solutions
- (optional) Any other lesson handouts

## Lesson Material
In general, lessons should have one or two core concepts that they're introducing.  Anything more than that leads to overload and an unproductive class.  Also in general, lessons should have practical exercises associated with the content material to reinforce understanding of the concepts. 

All content should be kept in its original format and only converted to pdf for archiving or presentation.  This makes it easier to edit long-term.

## Practical Exercises
The practical exercises should have instructions written in the markdown format and a solution guide also written in markdown format.  If the markdown format is not conducive, other formats such as .py or .ipynb files are acceptable.  Again, the idea is to keep the formatting as consistent as possible across mediums.  These files should be clearly labelled as the solution.

# Naming Conventions
- The only names that should be ordered are the lesson folders themselves, e.g. `Lesson01-XYZ`.  All other content should not be ordered.
- Classes and files should be named according to the topics that they cover.
- Use `CamelCase` for all folder and file names.

