'''
Created on 2014-10-16

@author: shsqkj
'''
# Import system modules
import os
import sys
import arcpy
from arcpy import env

from xml.dom import minidom 
from compiler.ast import Node
from platform import node
from ast import NodeVisitor

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
    
    return 
    
def addFieldToShapefile(filename,fieldname,fieldtype):
    # Execute AddField for new fields
    arcpy.AddField_management(sourceDir+"\\output\\"+filename,fieldname,fieldtype)
    print fieldname
    
    return

def readXML(xmlfilename,shpfilename):
    xmlDoc = minidom.parse(sourceDir+"\\input\\"+xmlfilename)
    items = xmlDoc.getElementsByTagName("item")
    #=print rootNode.toxml()
    # Create insert cursor for table 
    # 
    rows = arcpy.InsertCursor(sourceDir+"\\output\\"+shpfilename)
    fc = sourceDir+"\\output\\"+shpfilename
    #cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY"])
    for item in items:
#         row = rows.newRow()
        scenicName = item.getElementsByTagName("scenicname")[0]
#         row.NAME = scenicName.firstChild.data
        print "scenicname:" + scenicName.firstChild.data
        scenicLng = item.getElementsByTagName("lng")[0]
#         row.LNG = scenicLng.firstChild.data
        print "lng:" +scenicLng.firstChild.data
        scenicLat = item.getElementsByTagName("lat")[0]
#         row.LAT = scenicLat.firstChild.data
        print "lat:" + scenicLat.firstChild.data
        scenicFrom = item.getElementsByTagName("from")[0]
#         row.FROM_ = scenicFrom.firstChild.data
        print "from:" +scenicFrom.firstChild.data
#         rows.insertRow(row)
        xy = (scenicLng.firstChild.data, scenicLat.firstChild.data)
        #cursor.insertRow([xy])
    return
#createShapefile(sourceDir,"scenic_point.shp")

# addFieldToShapefile("scenic_point.shp","NAME","TEXT")
# addFieldToShapefile("scenic_point.shp","LNG","DOUBLE")
# addFieldToShapefile("scenic_point.shp","LAT","DOUBLE")
# addFieldToShapefile("scenic_point.shp","FROM","TEXT")

readXML("data_with_location_final.xml","scenic_point.shp")




