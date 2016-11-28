---

layout: default
title: Advanced Statistical Computing

---

# Bios 8366 Final Project

Bios 8366 students are introduced to a range of modern methods for optimization, machine learning, and probabilistic modeling. In addition to the assignments and in-class examples, it is beneficial for practitioners to gain experience using these techniques in a more realistic setting, using data that are collected for use in real-world biostatistical applications. Hence, 50% of the final grade in Bios 8366 will be determined by students' performance in a course project.

Students will allocate themselves to groups of 2 or 3. Each group will be given access to a Box.com link containing the project data. Completed projects should be pushed to the repository (**without the data**) no later than noon on Friday, Dec. 16, 2015. All students in a group will receive the same project grade.

### Prediction of readmission from Vanderbilt Hospitalization Data

The Vanderbilt hospital data is an extraction of 10,000 subjects from the [synthetic derivative](https://victr.vanderbilt.edu/pub/biovu/), which is broken down into 9 tables in comma-separated values (CSV) format, each linked via a deidentified subject ID (`RUID`). These data tables include:

`phenotype`
: Patient attributes, including sex, race, and dates of birth and death.  

`BMI`
: Body mass index measurement information.

`MED`
: Medications information, including dose and duration.

`LAB`
: Lab results, including lab name, date and result.

`CPT`
: Procedure codes for reporting medical procedures. This will provide information on procedures each patient underwent at Vanderbilt. You can look up individual codes online, using the [AMA search tool](https://ocm.ama-assn.org/OCM/CPTRelativeValueSearch.do?submitbutton=accept).

`ICD9`
: Coding of diagnosed diseases and health problems. This is an international standard for classifying diseases, including nuanced classifications of a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances, and external causes of injury or disease. The codes can be looked up on a [variety](http://www.cms.gov/medicare-coverage-database/staticpages/icd-9-code-lookup.aspx) [of places](http://www.wikiwand.com/en/List_of_ICD-9_codes) [online](http://icd9cm.chrisendres.com); there is even an iOS app for looking up ICD9 and CPT codes.

`eGFR`
: Estimated Glomerular Filtration Rate measurements, used to screen for kidney damage. Obtained from a creatine lab.

`BP`
: Blood pressure measurement information.

`ADT`
: Admit/Discharge/Transfer events.


**The objective of the Bios 8366 course project is to employ modeling tools introduced in this course to fit prediction models for patient readmission within 30 days of discharge using synthetic derivative data.**

Students may use any of the methods covered in the course syllabus, or any related methods, to develop candidate predictive models. Projects should include at least two alternative approaches, and each approach should be iteratively improved or tuned to yield the most competitive models.

The best projects will:

* include more supporting text than code: 
    + fully introduce problem
    + describe and justify selection of methods
    + discuss results and their implications
* include a reproducible workflow for cleaning and preparing data
* be runnable by anyone with access to the repository and the data
* use cross-validation and/or model selection methods, where appropriate
* make appropriate use of visualization tools
* include goodness-of-fit assessments, where appropriate
* report performance characteristics of models
* include opinions and recommendations based on output

The project reports should be pushed to GitHub by the project deadline. Final projects should be submitted as one or more iPython notebooks.

Finally, please add the following statement either to the end of the project or in the methods section when discussing the dataset:

> The dataset(s) used for the analyses described were obtained from Vanderbilt University Medical Center’s Synthetic Derivative which is supported by institutional funding and by the Vanderbilt CTSA grant ULTR000445 from NCATS/NIH
