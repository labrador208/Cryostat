# Cryostat

Look inside each file for more detailed explanations of how each program works. This readme says what to use them for.

CryostatTest1 is an outdated graphing program for graphing blackbody radiation curves at various temperatures from 300K to 0.1 K.

Cryostat2 is the updated version of CryostatTest1 with all graphs working correctly.

CryostatIntegration uses Monte Carlo integration to integrate under the blackbody radiation curves. The code can very quickly be modified to use on any other function that may come up in the future. See comments for how to modify.

CryostatGraphingFilter models how the blackbody radiation curves are affected by HDPE filters. Built in comparisons to the blackbody radiation curves without filters.

Zotefoam shows how the radiation curves are affected by a series of Zotefoam filters decreasing in temperature down to 50K.

ColdFilters shows radiation curves used on the coldest stages. 

Analysis for all 3 sets of filters is inside the documents.

Heat Loads Model is an Excel file showing how much heat will transfer between layers of the cryostat using formulas found online and some basic approximations. The calculated heat transfer is calculated by integrating across the entire spectrum of wavelengths. For finding heat transfer for a specific wavelength range, use the CryostatIntegration program and set the ranges as needed.

Most of the programs are currently in notebook form. I intend to put everything onto a single Python file that combines all of these functions and allows for easier use by simply inputting key variables like temperature, wavelength range, and types of filters used.

Update 8/27: New Files Heat Load Calculator, 8 Channel Record, and Temp Record have been added. 

Heat Load Calculator is the automated version of all aforementioned programs. Intended to be used in a way so that future cryostats are easier to model. Look inside for all functions.

Temp Record takes the readings from the Lakeshore Model 218 and outputs them to a text file. Reading the text file using KST and the settings of 8 Channel Record will display all of the data in graph form.
