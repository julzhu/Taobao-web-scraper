from tb_utils import *
import pandas as pd


set = pd.read_csv('lego_info.csv')
# print(set.shape)
# (1583, 5)

set = set[set['Shop'] == '乐高官方旗舰店'].drop_duplicates()
# filter official shop only
# print(set.shape)
# (554, 5)

prod_info = set['Product Name'].str.split(r'(\d+)')
set['Set_No'] = prod_info.apply(lambda x: x[1])
# extract set no.
sales_info = set['Sales'].str.split(r'(\d+)')
set['Sales'] = sales_info.apply(lambda x: x[1])
# extract set sales
print(set.head())

search = ('乐高' + set['Set_No']).to_list()

search = ['乐高76231', '乐高21337', '乐高60371', '乐高76210', '乐高80033', '乐高60350',
'乐高10297', '乐高41717', '乐高75330', '乐高75326', '乐高41957', '乐高75329', '乐高43203', '乐高60393', '乐高71374', '乐高75323',
'乐高41722', '乐高76943', '乐高75571', '乐高80043', '乐高10990', '乐高60373', '乐高75192', '乐高41743', '乐高41741', '乐高10316',
'乐高41728', '乐高21245', '乐高41729', '乐高41751', '乐高10304', '乐高75308', '乐高10292', '乐高76176', '乐高71374', '乐高71408',
'乐高71407', '乐高10789', '乐高10270', '乐高76946', '乐高60205', '乐高10312', '乐高10295', '乐高71411', '乐高10959', '乐高41962',
'乐高76207', '乐高11017', '乐高21057', '乐高10278', '乐高76956', '乐高21189', '乐高76989', '乐高76832', '乐高75313', '乐高71773']
# '乐高10963', '乐高71759', '乐高75349', '乐高60386', '乐高76420', '乐高41808', '乐高0', '乐高76909', '乐高42123', '乐高75979',
# '乐高42151', '乐高31133', '乐高10311', '乐高10280', '乐高10313', '乐高31208', '乐高60283', '乐高76206', '乐高42122', '乐高31058',
# '乐高76239', '乐高75551', '乐高76409', '乐高41703', '乐高60348', '乐高42154', '乐高10914', '乐高76247', '乐高21333', '乐高42137',
# '乐高10874', '乐高42096', '乐高42150', '乐高41168', '乐高42155', '乐高42107', '乐高92176', '乐高43192', '乐高42138', '乐高42135',
# '乐高80045', '乐高60373', '乐高76908', '乐高71395', '乐高75979', '乐高76392', '乐高41395', '乐高41393', '乐高60349', '乐高10698',
# '乐高42123', '乐高80040', '乐高60316', '乐高10899', '乐高71780', '乐高41711', '乐高76191', '乐高60374', '乐高76906', '乐高60375',
# '乐高76907', '乐高21327', '乐高71738', '乐高21056', '乐高76917', '乐高42153', '乐高42139', '乐高42149', '乐高10313', '乐高42130',
# '乐高10696', '乐高71784', '乐高10309', '乐高76918', '乐高10969', '乐高71043', '乐高10954', '乐高42151', '乐高76911', '乐高10931',
# '乐高76914', '乐高80033', '乐高21332', '乐高42143', '乐高10314', '乐高42147', '乐高60369', '乐高41742', '乐高80012', '乐高10280',
# '乐高76391', '乐高31143', '乐高60312', '乐高10298', '乐高42127', '乐高10914', '乐高76242', '乐高71785', '乐高71765', '乐高10316',
# '乐高60371', '乐高21034', '乐高76406', '乐高31208', '乐高76217', '乐高630', '乐高10311', '乐高80110', '乐高43197', '乐高75551',
# '乐高42122', '乐高21318', '乐高31133', '乐高21323', '乐高76910', '乐高42107', '乐高60350', '乐高21338', '乐高10975', '乐高42125',
# '乐高71034', '乐高75325', '乐高76239', '乐高80039', '乐高10271', '乐高60319', '乐高80041', '乐高10913', '乐高76223', '乐高76399',
# '乐高76206', '乐高71786', '乐高76241', '乐高41964', '乐高41715', '乐高76916', '乐高43205', '乐高76389', '乐高21334', '乐高42137',
# '乐高21185', '乐高21044', '乐高71770', '乐高71763', '乐高10875', '乐高10297', '乐高10935', '乐高76243', '乐高41450', '乐高76915',
# '乐高42148', '乐高10944', '乐高10411', '乐高43189', '乐高10941', '乐高42138', '乐高43194', '乐高71037', '乐高60315', '乐高76230',
# '乐高71800', '乐高76912', '乐高76225', '乐高71782', '乐高43207', '乐高10990', '乐高42110', '乐高10780', '乐高71781', '乐高31140',
# '乐高43214', '乐高31134', '乐高10279', '乐高60348', '乐高80043', '乐高42152', '乐高10302', '乐高71762', '乐高71766', '乐高10292',
# '乐高71036', '乐高42115', '乐高76240', '乐高60337', '乐高71032', '乐高75344', '乐高10986', '乐高60356', '乐高21058', '乐高41716',
# '乐高71788', '乐高71768', '乐高21333', '乐高71413', '乐高60335', '乐高60314', '乐高76220', '乐高75333', '乐高21326', '乐高76909',
# '乐高92176', '乐高42130', '乐高60392', '乐高80111', '乐高43210', '乐高41696', '乐高71772', '乐高41699', '乐高60351', '乐高60370',
# '乐高76409', '乐高41730', '乐高42139', '乐高60383', '乐高60304', '乐高80045', '乐高10874', '乐高71395', '乐高76247', '乐高41450',
# '乐高80032', '乐高71769', '乐高10962', '乐高75572', '乐高43202', '乐高80008', '乐高41395', '乐高42140', '乐高42134', '乐高71374',
# '乐高76244', '乐高76400', '乐高10295', '乐高60336', '乐高76407', '乐高60320', '乐高76392', '乐高43197', '乐高41703', '乐高76248',
# '乐高76245', '乐高10882', '乐高21329', '乐高42145', '乐高71774', '乐高80012', '乐高71043', '乐高10314', '乐高43216', '乐高60372',
# '乐高76908', '乐高43192', '乐高10979', '乐高76402', '乐高76408', '乐高76951', '乐高43199', '乐高10266', '乐高42155', '乐高76391',
# '乐高42143', '乐高42125', '乐高75576', '乐高10312', '乐高75575', '乐高60341', '乐高76900', '乐高10899', '乐高71756', '乐高31131',
# '乐高10303', '乐高31207', '乐高76945', '乐高42096', '乐高42154', '乐高21338', '乐高41732', '乐高75192', '乐高31135', '乐高31136',
# '乐高80037', '乐高60346', '乐高21335', '乐高41168', '乐高41711', '乐高76950', '乐高31201', '乐高76210', '乐高71360', '乐高76949',
# '乐高76181', '乐高41801', '乐高41714', '乐高71775', '乐高71411', '乐高71786', '乐高60374', '乐高41735', '乐高76830', '乐高71783',
# '乐高42141', '乐高60309', '乐高21337', '乐高10872', '乐高10973', '乐高21244', '乐高11020', '乐高10978', '乐高75317', '乐高11014',
# '乐高80109', '乐高75338', '乐高42110', '乐高21327', '乐高42153', '乐高42150', '乐高41743', '乐高41723', '乐高21243', '乐高31128',
# '乐高41711', '乐高41809', '乐高31138', '乐高60283', '乐高42139', '乐高41713', '乐高11021', '乐高76216', '乐高71776', '乐高10713',
# '乐高41720', '乐高76209', '乐高75327', '乐高71765', '乐高60349', '乐高41802', '乐高10290', '乐高71785', '乐高76918', '乐高60316',
# '乐高41727', '乐高41807', '乐高71764', '乐高10968', '乐高60385', '乐高41705', '乐高10984', '乐高76389', '乐高76191', '乐高60317',
# '乐高21336', '乐高60321', '乐高75328', '乐高71035', '乐高75308', '乐高75578', '乐高41739', '乐高43206', '乐高76208', '乐高80034',
# '乐高21241', '乐高21325', '乐高42127', '乐高10309', '乐高60338', '乐高31132', '乐高21332', '乐高42115', '乐高10272', '乐高80044',
# '乐高43211', '乐高10497', '乐高76218', '乐高60387', '乐高60384', '乐高60390', '乐高31137', '乐高21330', '乐高41742', '乐高75335',
# '乐高75336', '乐高41740', '乐高75577', '乐高31203', '乐高42144', '乐高21186', '乐高80036', '乐高21242', '乐高60337', '乐高41708',
# '乐高75573', '乐高75574', '乐高76211', '乐高71738', '乐高31130', '乐高10299', '乐高60394', '乐高80035', '乐高10971', '乐高42131',
# '乐高75337', '乐高31205', '乐高10411', '乐高42129', '乐高41733', '乐高21188', '乐高76948', '乐高75322', '乐高10283', '乐高10300',
# '乐高60351', '乐高21187', '乐高76832', '乐高75334', '乐高21190', '乐高21328', '乐高60373', '乐高21323', '乐高75579', '乐高10316',
# '乐高10298', '乐高76831', '乐高41738', '乐高41755', '乐高41961', '乐高76389', '乐高76399', '乐高10308', '乐高71403', '乐高80039',
# '乐高76413', '乐高76405', '乐高60389', '乐高76420', '乐高71033', '乐高21056', '乐高10698', '乐高76944', '乐高80111', '乐高71387',
# '乐高10273', '乐高10776', '乐高41712', '乐高76947', '乐高75304', '乐高10875', '乐高71036', '乐高71406', '乐高76212', '乐高10990',
# '乐高76917', '乐高10977', '乐高41724', '乐高71787', '乐高71414', '乐高41731', '乐高10306', '乐高10899', '乐高41947', '乐高10789',
# '乐高10982', '乐高60342', '乐高80110', '乐高76210', '乐高10278', '乐高80033', '乐高76956', '乐高80038', '乐高10255', '乐高41805',
# '乐高71771', '乐高75332', '乐高43204', '乐高10302']



file_name = 'lego_sales'
# update file name
max_page = 2
# update max search page

save(['Product Name', 'Price', 'Sales', 'Shop', 'Search Content'], file_name)
url = 'https://s.taobao.com/search?q=iPad'
driver.get(url)
driver.implicitly_wait(30)
# delay for manual login

for i in search:
    driver.find_element(By.ID, "q").clear()
    # clear search box
    driver.find_element(By.ID, "q").send_keys(i)
    # input search content
    driver.find_element(By.XPATH,
                        '//*[(@id = "J_SearchForm")]//*[contains(concat( " ", @class, " " ), concat( " ", "icon-btn-search", " " ))]').click()
    # click search button
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[contains(concat( " ", @class, " " ), concat( " ", "sort", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "link", " " ))]').click()
    # sort sales from high to low
    time.sleep(5)
    get_info(i, driver.current_url, 1, max_page, file_name)
    time.sleep(20)


