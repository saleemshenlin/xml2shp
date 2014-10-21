xml2shp
=======

使用arcpy，将xml文件转换为shapefile文件

1. arcpy.CreateFeatureclass_management()创建要素集

2. arcpy.AddField_management()加入字段

3. xml.dom.minidom.parse() 逐行读取xml
