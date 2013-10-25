---

layout: default
title: Advanced Statistical Computing

---

# Bios 366 Final Project

Bios 366 students are introduced to a range of modern methods for optimization, machine learning, and probabilistic modeling. In addition to the assignments and in-class examples, it is beneficial for practitioners to gain experience using these techniques in a more realistic setting, using data that are collected for use in real-world biostatistical applications. Hence, 50% of the final grade in Bios 366 will be determined by students' performance in a course project. 

Students will be allocated to groups of 2 or 3. Each group will be given access to a private GitHub repository containing the project data. Completed projects should be pushed to the repository no later than Dec. 5, 2013. All students in a group will receive the same project grade. 

### Prediction of Hospital Re-admission 

One metric for judging the quality of hospital care is the probability that patients experience unplanned readmission to hospital following a previous hospital stay. For example, a patient might be re-admitted for a surgical wound infection that occurred after an initial hospital stay. In 2013, as part of the Affordable Care Act, US lawmakers added language to the Social Security Act establishing the Hospital Readmissions Reduction Program, which penalizes hospitals with "excess readmissions". To comply with this program medical centers have begun developing predictive tools. The idea is to identify patients at high risk of readmission, so that the patient can undergo an in-hospital intervention to reduce the risk of readmission. *The objective of the Bios 366 course project is to employ modeling tools introduced in this course to fit prediction models for hospital readmission using Vanderbilt hospital records.*

Groups will be given a subset of records taken from Vanderbilt's Synthetic Derivative (SD), a database containing clinical information derived from Vanderbilt's electronic medical record. The SD is a set of records that is no longer linked to the identified medical record from which it is derived and has been altered (de-identified) to the point it no longer closely resembles the original record. The project dataset will include over 200 potential predictor variables, including demographic information, lab results, and survey responses, along with an indicator for readmission status. Students may use any of the methods covered in the course syllabus, or any related methods, to develop candidate predictive models. Projects should include at least two alternative approaches, and each approach should be iteratively improved or tuned to yield the most competitive models.

The dataset and project will be divided into two parts: first, two years of SD data will be provided for model fitting, and these finalized models should be committed to GitHub no later than Dec. 5. Second, a third year of data will be made available for testing out-of-sample prediction. The predictions and associated performance characteristics should be pushed to GitHub by the project deadline (Dec. 14). Final projects should be submitted as one or more iPython notebooks. 

All students must complete a Vanderbilt data use agreement before gaining access to the readmission dataset. 

In January, each group will present a 20-minute talk outlining the results of their project, and the methods used to derive them. The presentation will be mandatory for Biostatistics students and optional (but encouraged) for others. 

