'''
Created on 2014-10-16

@author: shsqkj
'''
# Import system modules
import os
import sys
import arcpy
from arcpy import env

#Set workspace
sourceDir = os.path.abspath(os.path.dirname(sys.argv[0]))    #source dir
env.workspace = sourceDir;

def createShapefile(path,filename):
    #Set local variables
    outPath = path + "/output"
    fileName = filename
    geometryType = "POINT"
    # Creating a spatial reference object
    spatialReference = arcpy.SpatialReference(path+"/projected/WGS1984.prj")

    # Execute CreateFeatureclass
    arcpy.CreateFeatureclass_management(outPath, fileName, geometryType, "#", "DISABLED", "DISABLED", spatialReference)
    print "Create Shapefile success!"
    
def addFieldToShapefile(filename,fieldname,fieldtype):
    # Execute AddField for new fields
    arcpy.AddField_management(sourceDir+"\\output\\"+filename,fieldname,fieldtype)
    print fieldname
    
#createShapefile(sourceDir,"scenic_point.shp")
addFieldToShapefile("scenic_point.shp","NAME","TEXT")
addFieldToShapefile("scenic_point.shp","LNG","DOUBLE")
addFieldToShapefile("scenic_point.shp","LAT","DOUBLE")
addFieldToShapefile("scenic_point.shp","FROM","TEXT")






