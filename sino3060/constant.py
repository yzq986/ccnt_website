data = """安徽省: 安庆市, 蚌埠市, 亳州市, 池州市, 滁州市, 阜阳市, 合肥市, 淮北市, 淮南市, 黄山市, 六安市, 马鞍山市, 宿州市, 铜陵市, 芜湖市, 宣城市
福建省: 福州市, 龙岩市, 南平市, 宁德市, 莆田市, 泉州市, 三明市, 厦门市, 漳州市
甘肃省: 白银市, 定西市, 甘南藏族自治州, 嘉峪关市, 金昌市, 酒泉市, 兰州市, 临夏回族自治州, 陇南市, 平凉市, 庆阳市, 天水市, 武威市, 张掖市
广东省: 潮州市, 东莞市, 东沙群岛市, 佛山市, 广州市, 河源市, 惠州市, 江门市, 揭阳市, 茂名市, 梅州市, 清远市, 汕头市, 汕尾市, 韶关市, 深圳市, 阳江市, 云浮市, 湛江市, 肇庆市, 中山市, 珠海市
广西壮族自治区: 百色市, 北海市, 崇左市, 防城港市, 贵港市, 桂林市, 河池市, 贺州市, 来宾市, 柳州市, 南宁市, 钦州市, 梧州市, 玉林市
贵州省: 安顺市, 毕节市, 贵阳市, 六盘水市, 黔东南苗族侗族自治州, 黔南布依族苗族自治州, 黔西南布依族苗族自治州, 铜仁市, 遵义市
海南省: 白沙黎族自治县, 保亭黎族苗族自治县, 昌江黎族自治县, 澄迈县市, 儋州市, 定安县市, 东方市, 海口市, 乐东黎族自治县, 临高县市, 陵水黎族自治县, 琼海市, 琼中黎族苗族自治县, 三沙市, 三亚市, 屯昌县市, 万宁市, 文昌市, 五指山市
河北省: 保定市, 承德市, 邯郸市, 衡水市, 廊坊市, 秦皇岛市, 石家庄市, 唐山市, 邢台市, 张家口市
河南省: 安阳市, 沧州市, 鹤壁市, 济源市, 焦作市, 开封市, 洛阳市, 南阳市, 平顶山市, 濮阳市, 三门峡市, 商丘市, 漯河市, 新乡市, 信阳市, 许昌市, 郑州市, 周口市, 驻马店市
黑龙江省: 大庆市, 大兴安岭地区, 哈尔滨市, 鹤岗市, 黑河市, 鸡西市, 佳木斯市, 牡丹江市, 七台河市, 齐齐哈尔市, 双鸭山市, 绥化市, 伊春市
湖北省: 鄂州市, 恩施土家族苗族自治州, 黄冈市, 黄石市, 荆门市, 荆州市, 潜江市, 神农架林区, 十堰市, 随州市, 天门市, 武汉市, 仙桃市, 咸宁市, 襄阳市, 孝感市, 宜昌市
湖南省: 常德市, 长沙市, 郴州市, 衡阳市, 怀化市, 娄底市, 邵阳市, 湘潭市, 湘西土家族苗族自治州, 益阳市, 永州市, 岳阳市, 张家界市, 株洲市
吉林省: 白城市, 白山市, 长春市, 吉林市, 辽源市, 四平市, 松原市, 通化市, 延边朝鲜族自治州
江苏省: 常州市, 淮安市, 连云港市, 南京市, 南通市, 苏州市, 宿迁市, 泰州市, 无锡市, 徐州市, 盐城市, 扬州市, 镇江市
江西省: 抚州市, 赣州市, 吉安市, 景德镇市, 九江市, 南昌市, 萍乡市, 上饶市, 新余市, 宜春市, 鹰潭市
辽宁省: 鞍山市, 本溪市, 大连市, 丹东市, 抚顺市, 阜新市, 葫芦岛市, 锦州市, 辽阳市, 盘锦市, 沈阳市, 铁岭市, 营口市, 朝阳市
内蒙古自治区: 阿拉善盟, 巴彦淖尔市, 包头市, 赤峰市, 鄂尔多斯市, 呼和浩特市, 呼伦贝尔市, 通辽市, 乌海市, 乌兰察布市, 锡林郭勒盟, 兴安盟
宁夏回族自治区: 固原市, 石嘴山市, 吴忠市, 银川市, 中卫市
青海省: 果洛藏族自治州, 海北藏族自治州, 海东市, 海南藏族自治州, 海西蒙古族藏族自治州, 黄南藏族自治州, 西宁市, 玉树藏族自治州
山东省: 滨州市, 德州市, 东营市, 菏泽市, 济南市, 济宁市, 莱芜市, 聊城市, 临沂市, 青岛市, 日照市, 泰安市, 威海市, 潍坊市, 烟台市, 枣庄市, 淄博市
山西省: 长治市, 大同市, 晋城市, 晋中市, 临汾市, 吕梁市, 朔州市, 太原市, 忻州市, 阳泉市, 运城市
陕西省: 安康市, 宝鸡市, 汉中市, 商洛市, 铜川市, 渭南市, 西安市, 咸阳市, 延安市, 榆林市
四川省: 阿坝藏族羌族自治州, 巴中市, 成都市, 达州市, 德阳市, 甘孜藏族自治州, 广安市, 广元市, 乐山市, 凉山彝族自治州, 泸州市, 眉山市, 绵阳市, 南充市, 内江市, 攀枝花市, 遂宁市, 雅安市, 宜宾市, 资阳市, 自贡市
西藏自治区: 阿里地区, 昌都市, 拉萨市, 林芝市, 那曲地区, 日喀则市, 山南市
新疆维吾尔自治区: 阿克苏地区, 阿拉尔市, 阿勒泰地区, 巴音郭楞蒙古自治州, 北屯市, 博尔塔拉蒙古自治州, 昌吉回族自治州, 哈密市, 和田地区, 喀什地区, 可克达拉市, 克拉玛依市, 克孜勒苏柯尔克孜自治州, 昆玉市, 石河子市, 双河市, 塔城地区, 铁门关市, 图木舒克市, 吐鲁番市, 乌鲁木齐市, 五家渠市, 伊犁哈萨克自治州
云南省: 保山市, 楚雄彝族自治州, 大理白族自治州, 德宏傣族景颇族自治州, 迪庆藏族自治州, 红河哈尼族彝族自治州, 昆明市, 丽江市, 临沧市, 怒江傈僳族自治州, 普洱市, 曲靖市, 文山壮族苗族自治州, 西双版纳傣族自治州, 玉溪市, 昭通市
浙江省: 杭州市, 湖州市, 嘉兴市, 金华市, 丽水市, 宁波市, 衢州市, 绍兴市, 台州市, 温州市, 舟山市
上海市: 嘉定区, 奉贤区, 宝山区, 崇明区, 徐汇区, 普陀区, 杨浦区, 松江区, 浦东新区, 虹口区, 金山区, 长宁区, 闵行区, 青浦区, 静安区, 黄浦区
香港特别行政区: 东区, 中西区, 九龙城区, 元朗区, 北区, 南区, 大埔区, 屯门区, 沙田区, 油尖旺区, 深水埗区, 湾仔区, 离岛区, 荃湾区, 葵青区, 西贡区, 观塘区, 黄大仙区
北京市: 东城区, 丰台区, 大兴区, 密云区, 平谷区, 延庆区, 怀柔区, 房山区, 昌平区, 朝阳区, 海淀区, 石景山区, 西城区, 通州区, 门头沟区, 顺义区
澳门特别行政区: 嘉模堂区, 圣方济各堂区, 大堂区, 望德堂区, 花地玛堂区, 花王堂区, 路凼填海区, 风顺堂区
重庆市: 万州区, 丰都县, 九龙坡区, 云阳县, 北碚区, 南岸区, 南川区, 合川区, 垫江县, 城口县, 大渡口区, 大足区, 奉节县, 巫山县, 巫溪县, 巴南区, 开州区, 彭水苗族土家族自治县, 忠县, 梁平县, 武隆县, 永川区, 江北区, 江津区, 沙坪坝区, 涪陵区, 渝中区, 渝北区, 潼南区, 璧山区, 石柱土家族自治县, 秀山土家族苗族自治县, 綦江区, 荣昌区, 酉阳土家族苗族自治县, 铜梁区, 长寿区, 黔江区
天津市: 东丽区, 北辰区, 南开区, 和平区, 宁河区, 宝坻区, 武清区, 河东区, 河北区, 河西区, 津南区, 滨海新区, 红桥区, 蓟州区, 西青区, 静海区
"""

data_en = """Anhui: Anqing, Bengbu, Bozhou, Chizhou, Chuzhou, Fuyang, Hefei, Huaibei, Huainan, Huangshan, Lu'an, Ma'anshan, Suzhou, Tongling, Wuhu, Xuan
Fujian: Fuzhou, Longyan, Nanping, Ningde, Putian, Quanzhou, Sanming, Xiamen, Zhangzhou
Gansu: Baiyin, Dingxi, Gannan Tibetan Autonomous Prefecture, Jiayuguan, Jinchang, Jiuquan, Lanzhou, Linxia Hui Autonomous Prefecture, Longnan, Pingliang, Qingyang, Tianshui, Wuwei, Zhangye
Guangdong: Chaozhou, Dongguan, Dongsha Islands, Foshan, Guangzhou, Heyuan, Huizhou, Jiangmen, Jieyang, Maoming, Meizhou, Qingyuan, Shantou, Shanwei, Shaoguan, Shenzhen, Yangjiang, Yunfu, Zhanjiang, Zhaoqing, Zhongshan, Zhuhai
Guangxi Zhuang: Baise, Beihai, Chongzuo, Fangchenggang, Guigang, Guilin, Hechi, Hezhou, Laibin, Liuzhou, Nanning, Qinzhou, Wuzhou, Yulin
Guizhou: Anshun, Bijie, Guiyang, Liupanshui, Qiandongnan Miao and Dong Autonomous Prefecture, Qiannan Buyi and Miao Autonomous Prefecture, Qianxinan Buyi and Miao Autonomous Prefecture, Tongren, Zunyi
Hainan: Baisha Li Autonomous County, Baoting Li and Miao Autonomous County, Changjiang Li Autonomous County, Chengmai County, Danzhou, Ding'an County, Dongfang, Haikou, Ledong Li Autonomous County, Lingao County, Lingshui Li Autonomous County, Qionghai, Qiongzhong Li and Miao Autonomous County, Sansha, Sanya, Tunchang County, Wanning, Wenchang, Wuzhishan
Hebei: Baoding, Chengde, Handan, Hengshui, Langfang, Qinhuangdao, Shijiazhuang, Tangshan, Xingtai, Zhangjiakou
Henan: Anyang, Cangzhou, Hebi, Jiyuan, Jiaozuo, Kaifeng, Luoyang, Nanyang, Pingdingshan, Puyang, Sanmenxia, Shangqiu, Luohe, Xinxiang, Xinyang, Xuchang, Zhengzhou, Zhoukou, Zhumadian
Heilongjiang: Daqing, Greater Khingan Mountains, Harbin, Hegang, Heihe, Jixi, Jiamusi, Mudanjiang, Qitaihe, Qiqihar, Shuangyashan, Suihua, Yichun
Hubei: Ezhou, Enshi Tujia and Miao Autonomous Prefecture, Huanggang, Huangshi, Jingmen, Jingzhou, Qianjiang, Shennongjia Forest District, Shiyan, Suizhou, Tianmen, Wuhan, Xiantao, Xianning, Xiangyang, Xiaogan, Yichang
Hunan: Changde, Changsha, Chenzhou, Hengyang, Huaihua, Loudi, Shaoyang, Xiangtan, Xiangxi Tujia and Miao Autonomous Prefecture, Yiyang, Yongzhou, Yueyang, Zhangjiajie, Zhuzhou
Jilin: Baicheng, Baishan, Changchun, Jilin, Liaoyuan, Siping, Songyuan, Tonghua, Yanbian Korean Autonomous Prefecture
Jiangsu: Changzhou, Huaian, Lianyungang, Nanjing, Nantong, Suzhou, Suqian, Taizhou, Wuxi, Xuzhou, Yancheng, Yangzhou, Zhenjiang
Jiangxi: Fuzhou, Ganzhou, Ji'an, Jingdezhen, Jiujiang, Nanchang, Pingxiang, Shangrao, Xinyu, Yichun, Yingtan
Liaoning: Anshan, Benxi, Dalian, Dandong, Fushun, Fuxin, Huludao, Jinzhou, Liaoyang, Panjin, Shenyang, Tieling, Yingkou, Chaoyang
Inner Mongolia: Alxa League, Bayannaoer, Baotou, Chifeng, Ordos, Hohhot, Hulunbuir, Tongliao, Wuhai, Ulanqab, Xilin Gol League, Xing'an League
Ningxia: Guyuan, Shizuishan, Wuzhong, Yinchuan, Zhongwei
Qinghai: Guoluo Tibetan Autonomous Prefecture, Haibei Tibetan Autonomous Prefecture, Haidong, Hainan Tibetan Autonomous Prefecture, Haixi Mongolian Tibetan Autonomous Prefecture, Huangnan Tibetan Autonomous Prefecture, Xining, Yushu Tibetan Autonomous Prefecture
Shandong: Binzhou, Dezhou, Dongying, Heze, Jinan, Jining, Laiwu, Liaocheng, Linyi, Qingdao, Rizhao, Tai'an, Weihai, Weifang, Yantai, Zaozhuang, Zibo
Shanxi: Changzhi, Datong, Jincheng, Jinzhong, Linfen, Luliang, Shuozhou, Taiyuan, Xinzhou, Yangquan, Yuncheng
Shaanxi: Ankang, Baoji, Hanzhong, Shangluo, Tongchuan, Weinan, Xi'an, Xianyang, Yan'an, Yulin
Sichuan: Aba Tibetan and Qiang Autonomous Prefecture, Bazhong, Chengdu, Dazhou, Deyang, Ganzi Tibetan Autonomous Prefecture, Guang'an, Guangyuan, Leshan, Liangshan Yi Autonomous Prefecture, Luzhou, Meishan, Mianyang, Nanchong, Neijiang, Panzhihua, Suining, Ya'an, Yibin, Ziyang, Zigong
Tibet: Ngari Region, Changdu, Lhasa, Nyingchi, Naqu Region, Shigatse, Shannan
Xinjiang: Aksu Region, Alar, Altay Region, Bayingolen Mongolian Autonomous Prefecture, Beitun, Bortala Mongolian Autonomous Prefecture, Changji Hui Autonomous Prefecture, Hami, Hotan Region, Kashgar Region, Kekedala, Karamay, Kizilsu Kirgiz Autonomous Prefecture, Kunyu, Shihezi, Shuanghe, Tacheng District, Tiemenguan, Tumushuk, Turpan, Urumqi, Wujiaqu, Ili Kazakhstan autonomous prefecture
Yunnan: Baoshan, Chuxiong Yi Autonomous Prefecture, Dali Bai Autonomous Prefecture, Dehong Dai and Jingpo Autonomous Prefecture, Diqing Tibetan Autonomous Prefecture, Honghe Hani and Yi Autonomous Prefecture, Kunming, Lijiang, Lincang, Nujiang Lisu Autonomous Prefecture, Puer, Qujing, Wenshan Zhuang and Miao Autonomous Prefecture, Xishuangbanna Dai Autonomous Prefecture, Yuxi, Zhaotong
Zhejiang: Hangzhou, Huzhou, Jiaxing, Jinhua, Lishui, Ningbo, Quzhou, Shaoxing, Taizhou, Wenzhou, Zhoushan
Shanghai: Jiading, Fengxian, Baoshan, Chongming, Xuhui, Putuo, Yangpu, Songjiang, Pudong, Hongkou, Jinshan, Changning, Minhang, Qingpu, Jing'an, Huangpu
Hong Kong: Eastern, Central and Western, Kowloon City, Yuen Long, North, Southern, Tai Po, Tuen Mun, Sha Tin, Yau Tsim Mong, Sham Shui Po, Wan Chai, Outlying Islands, Tsuen Wan, Kwai Tsing, Sai Kung, Kwun Tong, Wong Tai Sin
Beijing: Dongcheng, Fengtai, Daxing, Miyun, Pinggu, Yanqing, Huairou, Fangshan, Changping, Chaoyang, Haidian, Shijingshan, Xicheng, Tongzhou, Mentougou, Shunyi
Macau: Carmo Parish, St. Francis Parish, Lobby Area, Wangde Parish, Fatima Parish, Kao Parish, Cotai Reclamation Area, Fengshun Parish
Chongqing: Wanzhou, Fengdu County, Jiulongpo, Yunyang County, Beibei, Nan'an, Nanchuan, Hechuan, Dianjiang County, Chengkou County, Dadukou, Dazu, Fengjie County, Wushan County, Wuxi County, Banan, Kaizhou, Pengshui Miao and Tujia Autonomous County, Zhong County, Liangping County, Wulong County, Yongchuan, Jiangbei, Jiangjin, Shapingba, Fuling, Yuzhong, Yubei, Tongnan, Bishan, Shizhu Tujia and Miao Autonomous County, Xiushan Tujia and Miao Autonomous County, Qijiang, Rongchang, Youyang Tujia and Miao Autonomous County, Tongliang, Changshou, Qianjiang
Tianjin: Dongli, Beichen, Nankai, Heping, Ninghe, Baodi, Wuqing, Hedong, Hebei, Hexi, Jinnan, Binhai New, Hongqiao, Jizhou, Xiqing, Jinghai
"""

province2cities = {}
city2province = {}
province_cn2en = {}
city_cn2en = {}
for line, line_en in zip(data.split("\n"), data_en.split("\n")):
    if not line:
        continue
    province, cities = line.split(": ")
    province_en, cities_en = line_en.split(": ")
    cities = cities.split(", ") if cities != '' else []
    cities_en = cities_en.split(", ") if cities_en != '' else []
    province2cities[province] = cities
    province_cn2en[province] = province_en
    for city, city_en in zip(cities, cities_en):
        if city != "":
            city2province[city] = province
            city_cn2en[city] = city_en

# print(province2cities)
# print(city2province)
# print(province_cn2en)
# print(city_cn2en)

city_cn2en_ = city_cn2en.copy()
for k, v in city_cn2en.items():
    city_cn2en_[k] = v + '(' + k + ')'
# print(city_cn2en_)