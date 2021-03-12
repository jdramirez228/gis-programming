# Name: Diego Ramirez
# GEOG 196G MW 9:00AM
# Due: 04/06/2020
#
# Lab 9.3 - SelectLayerByLocation_management()

# Import modules
import arcpy

# Set variables 
in_features = "fedlanp020_CA" 
subsetArea = "seqmead92"

# Select all polygons in fedlanp020_CA that contains the meadows in ‘seqmead92’
subset = arcpy.SelectLayerByLocation_management(inFeatures, "intersect", subsetArea, 0, "new_selection") 

# Save the selection as ‘fedlanp020_mead92’
arcpy.CopyFeatures_management(in_features, "fedlanp020_mead92")
