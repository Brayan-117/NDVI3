import os
from osgeo import gdal, gdal_array

os.chdir("C:\Users\20154982\Desktop\gap_mask")
print (os.listdir(os.getcwd()))

NIR = iface.addRasterLayer('L71029047_04720091114_B50.TIF','NIR')
RED = iface.addRasterLayer('L71029047_04720091114_B30.TIF','RED')

import processing

NIR = processing.getObjectFromName("NIR")
Red = processing.getObjectFromName("RED")

NVDI_syntax = '(A-B)/(A+B)'

outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', 
                                                    NIR,         #INPUT_A
<ParameterRaster>
                                                    '1',         #BAND_A
<ParameterString>
                                                    RED,         #INPUT_B
<ParameterRaster>
                                                    '1',         #BAND_B
<ParameterString>
                                                    None,        #INPUT_C
<ParameterRaster>
                                                    '1',         #BAND_C
<ParameterString>
                                                    None,        #INPUT_D
<ParameterRaster>
                                                    '1',         #BAND_D
<ParameterString>
                                                    None,        #INPUT_E
<ParameterRaster>
                                                    '1',         #BAND_E
<ParameterString>
                                                    None,        #INPUT_F
<ParameterRaster>
                                                    '1',         #BAND_F
<ParameterString>
                                                    NDVI_syntax, #FORMULA
<ParameterString>
                                                    '',          #NO_DATA
<ParameterString>
                                                    5,           #RTYPE
<ParameterSelection>
                                                    '0',         #EXTRA
<ParameterString>
                                                    None)        #OUTPUT
<OutputRaster>

NDVI = QgsRasterLayer(outputs_GDALOGRRASTERCALCULATOR_1['OUTPUT'],'NDVI')

QgsMapLayerRegistry.instance().addMapLayer(NDVI)
