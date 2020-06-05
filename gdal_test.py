from osgeo import gdal

data_set = gdal.Open("G:/产品/数管/网上下载的数据/GF1_PMS1_E103.8_N33.3_20170115_L1A0002122491/"
                     "GF1_PMS1_E103.8_N33.3_20170115_L1A0002122491-MSS1.tiff")

# print("输入图像的路径", data_set.GetDescription())  # 获取输入图像路径
# print("bands:", data_set.RasterCount)  # 波段数
# cols = data_set.RasterXSize  # 图像长度
# print("cols:", cols)
# rows = data_set.RasterYSize  # 图像宽度
# print("rows:", rows)
#
# Coordinate_system = data_set.GetProjection()  # 获取坐标系
# print("Coordinate_system：", Coordinate_system)
# # print(data_path.GetRasterDataType())  # 获取数据类型

print("Driver: {}/{}".format(data_set.GetDriver().ShortName, data_set.GetDriver().LongName))
print("Size is {} x {} x {}".format(data_set.RasterXSize,
                                    data_set.RasterYSize,
                                    data_set.RasterCount))
print("Projection is {}".format(data_set.GetProjection()))
Coordinate_system = data_set.GetGeoTransform()
if Coordinate_system:
    print("Origin = ({}, {})".format(Coordinate_system[0], Coordinate_system[3]))
    print("Pixel Size = ({}, {})".format(Coordinate_system[1], Coordinate_system[5]))

band = data_set.GetRasterBand(1)
print("Band Type={}".format(gdal.GetDataTypeName(band.DataType)))

min = band.GetMinimum()
max = band.GetMaximum()
if not min or not max:
    (min, max) = band.ComputeRasterMinMax(True)
print("Min={:.3f}, Max={:.3f}".format(min, max))

if band.GetOverviewCount() > 0:
    print("Band has {} overviews".format(band.GetOverviewCount()))

if band.GetRasterColorTable():
    print("Band has a color table with {} entries".format(band.GetRasterColorTable().GetCount()))
