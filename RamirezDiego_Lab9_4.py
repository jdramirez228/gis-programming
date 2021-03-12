import arcpy

featureClass = arcpy.GetParameterAsText(0)
stateField = arcpy.getParameterAsText(1)

whereClause = '"State" = \'CA\'' 
totalArea = 0

# Retrieve only rows which meet the SQL conditions
with arcpy.da.SearchCursor(featureClass, populationField, whereClause) as cursor:
    for row in cursor:
        totalArea += row.getValue(AREA)

print("The state \' %s\' has %s (units) of federal land" % (stateField, totalArea))
