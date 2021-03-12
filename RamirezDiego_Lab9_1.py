# Name: Diego Ramirez
# GEOG 196G MW 9:00AM
# Due: 04/06/2020
#
# Lab 9.1 - SelectLayerByAttribute_management()

# Import modules
import arcpy

# Set variables
in_features = "fedlanp020" 
whereClause = '"State" = \'CA\'' 

# Select all polygons in ‘fedlanp020’ that are in California. 
arcpy.SelectLayerByAttribute_management(in_features, "NEW_SELECTION", whereClause)

# Save the output to ‘fedlanp020_CA’ 
arcpy.CopyFeatures_management(in_features, "fedlanp020_CA")
