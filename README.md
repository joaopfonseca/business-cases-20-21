# business-cases

Repository for storing the business cases (i.e., projects) for the NOVA IMS
master course Business Cases

## Business cases' description

Whenever a new business case is made available, it is going to be provided
both in the course's moodle page as well as a Markdown file in its
corresponding folder, which will also contain the necessary data for you to
develop the project.

## (Suggested) Structure of a Business Case

A template for structuring the development of a business case is provided
in `BC0_template/`. Of course, this is simply a suggestion on a way to
structure the development of your business cases, you are free to structure
them however you like.

```
BC<X>_<name of business case>
├── analysis <---- Your visualizations, tables, diagrams, etc. should be
│                  stored here. These can come from any step of the CRISP-DM
│                  process.
│
├── content <----- Your report and presentation should be stored here. You may
│                  want to include the pdf version of those files (allows the
│                  preview of those documents directly in GitHub).
│
├── data <-------- Your datasets should be stored here. Feel free to separate
│                  your data in different directories:
│                  - raw (original, immutable data)
│                  - interim (intermediate preprocessing steps) 
│                  - processed (processed data)
│
├── description <- You may include the original business case and eventual 
│                  support materials here. Alternatively, just add the
│                  business case description to the README.md file.
│
├── scripts <----- Your scripts should be stored here. Aim to keep the
│                  different steps of your analyses in separate scripts. If
│                  you prefer to work with notebooks (although we recommend
│                  using scripts for the sake of ease of use and
│                  reproducibility)
│
└── README.md <--- You may use this file to store the problem description.
                   This is automatically displayed in on GitHub, making it
                   easier for anyone to understand the goals of this project.
```
