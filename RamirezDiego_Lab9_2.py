# Name: Diego Ramirez
# GEOG 196G MW 9:00AM
# Due: 04/06/2020
#
# Lab 9.2 - Select_analysis()

# Import modules
import arcpy

# Set variables 
in_features = "fedlanp020" 
whereClause = '"State" = \'CA\'' 

# Select all polygons in ‘fedlanp020’ that are in California. Save the output to ‘fedlanp020_CA2’.
arcpy.Select_analysis(in_features, "fedlanp020_CA2", whereClause)
