# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json
import time
import urllib.parse
from urllib.parse import quote
from baidu_music_test.data import api_parameter_data
from baidu_music_test.utils import log_utils


def __get_url(host='',method='',**kwargs):
    """功能：
            拼接出URL
        参数：
            host：例子：http://tingapi.ting.baidu.com/v1/restserver/ting?
            method：接口
            **kwargs：因为不同接口需要不同的参数，就要传入不同的参数，
        例子：
            具体的歌单页面需要：
            list_id（歌单id），offset=‘0’，withsong=‘1’，withcount=‘1’，size（返回的歌曲数量）=‘100’
        歌单页面需要：
            channelname（频道说明（用中文需要转码）），size=‘100’，offset=‘0’，order_type（排序方式0最新1最热）=‘1’
        榜单页面需要：
            type(具体是那个榜单，如：1是新歌榜，2是热歌榜，具体可以到api文档中查询：http://apidoc.taihenw.com/interface/info.php?interface_id=16)，
            offset='0',size='100',fields=''(这个是需要的字段，是一个长串，例子：song_id%2Ctitle%2Cauthor%2Calbum_title%2Cpic_big%2Cpic_small%2Chavehigh%2Call_rate%2Ccharge%2Chas_mv_mobile%2Clearn%2Csong_source%2Ckorean_bb_song)"""
    timestamp = int(time.time())        #获取时间戳


    base_parameter_list = {
        'from'  : api_parameter_data.from_android,
        'version' : api_parameter_data.version,
        'channel' : api_parameter_data.channel,
        'operator' : api_parameter_data.operator,
        'qa' : api_parameter_data.qa,
        'method' : method,
        'timestamp' : str(timestamp)
    }
    method_par = kwargs                 #可变参数串
    url = host+urllib.parse.urlencode(base_parameter_list)+'&'+urllib.parse.urlencode(method_par)
    #print('生成的url为：'+url)
    return url

def __get_info(url = '', number = 0):
    """功能：
            根据url获取页面json
        返回值：
            dic：正常的返回信息
            1：获取多次失败"""
    i = number
    page = urlopen(url)
    data = page.read()
    dic = json.loads(data)
    result = __check_result(dic)
    if result == 0:
        return dic
    elif (not result == 0) and i<3:
        i += 1
        log_utils.C_INFO('获取信息失败，第 %d 次重新获取信息' %i)
        if __get_info(url,i) == 1:
            return 1
    else:
        log_utils.F_ERROR('重新获取信息多次失败，请检查接口和url。URL：'+url)
        return 1

def __check_result(dic):
    """功能：
            验证错误码，打印对应信息
        返回值：
            0：正常
            1：参数错误"""
    error_code = dic['error_code']
    log_utils.C_INFO('error_code：'+str(error_code))
    if error_code == 22000:
        log_utils.C_INFO('获取信息成功')
        return 0
    elif error_code == 22005:
        log_utils.F_ERROR('获取信息失败。')
        log_utils.F_ERROR('error_message：'+dic['error_message'])
        return 1
    else:
        log_utils.F_ERROR('未知错误码')
        log_utils.F_ERROR('error_message：'+dic['error_message'])
        return 2

def __get_cookie():
    """login_id是账号，password是密码的md5加密"""
    url = 'http://passport.qianqian.com/login?login_id=13522113807&password=29eea60d91f9216d0ce950889eb637c9&device_id=v2pcweb-zkagfyuhly15132404684581&tpl=baidu_music&login_type=1'
    page = urlopen(url)
    data = page.read()
    dic = json.loads(data)
    if not dic['error_code'] == 0:
        log_utils.F_ERROR('获取token失败！错误码为：'+dic['error_code'])
        return 1

    token = dic['token']
    return token

def __get_first_list_id_from_playlist(mode,url = ''):
    """功能：
            获取对应歌单列表的一些信息
        参数：
            mode：返回的内容：1：获取对应歌单列表的第一个歌单list_id
                            2：获取对应歌单列表的第一个歌单的title
        返回值：
            1：获取失败
            """
    dic = __get_info(url)
    if dic == 1:
        log_utils.F_ERROR('获取信息失败')
        return 1

    if mode == 1:
        list_id = dic['diyInfo'][0]['list_id']
        log_utils.C_INFO('获取的list_id为：'+list_id)
        return list_id
    elif mode == 2:
        list_name = dic['diyInfo'][0]['title']
        return list_name

def __get_first_three_song_name_from_songlist(number,url = ''):
    """功能：
            获取新歌榜前number首歌曲名
        参数:
            url:
            number：获取的歌曲名数量
        返回值：
            1：获取失败"""
    dic = __get_info(url)
    if dic == 1:
        log_utils.F_ERROR('获取信息失败')
        return 1

    log_utils.C_INFO('该榜单的前 %d 首歌曲名为：'% number)
    song_name_list={}
    i=0
    while i < number:
        song_name_list[i] = dic['song_list'][i]['title']
        log_utils.C_INFO(str(i+1)+':'+song_name_list[i])
        i += 1
    return song_name_list

def __get_first_three_song_name_from_playlist(number,url = ''):
    """功能：
            获取对应url歌单的前number首歌曲名
        参数：
            number：获取的歌曲名数量
        返回值：
            1：获取失败"""

    dic = __get_info(url)
    if dic == 1:
        log_utils.F_ERROR('获取信息失败')
        return 1

    song_list_name = dic['result']['info']['list_title']
    log_utils.C_INFO('该歌单名为：'+song_list_name)
    song_name_list={}
    log_utils.C_INFO('该歌单的前 %d 首歌名为：'%number)
    i=0
    while i < number:
        song_name_list[i] = dic['result']['songlist'][i]['title']
        log_utils.C_INFO(str(i+1)+':'+song_name_list[i])
        i += 1
    return song_name_list

def __get_collector_user_id_list(url = ''):
    """获取收藏此歌单的用户id"""
    dic = __get_info(url)
    if dic == 1:
        log_utils.F_ERROR('获取信息失败')
        return 1
    collect_num  = dic['result']['collect_num']
    i=0
    user_id_list = {}
    if collect_num > 7:
        while i < collect_num:
            user_id_list[i] = dic['result']['collector'][i]['userid']
            i += 1
    else:
        while i < 7:
            user_id_list[i] = dic['result']['collector'][i]['userid']
            i += 1
    return user_id_list

def __get_first_song_have_mv_code(play_list_url):
    """根据url获取对应歌单的第一首歌的has_mv的code
    返回值：
        1：获取失败
        “1”：有mv
        “0”：没有mv"""
    dic = __get_info(play_list_url)
    if dic == 1:
        log_utils.F_ERROR('获取信息失败')
        return 1
    has_mv_code = dic['result']['songlist'][0]['has_mv']
    return has_mv_code

def get_new_song_list_first_song_name(number):
    """获取新歌榜的前number首歌曲的歌曲名
    返回值：
        song_list：歌曲名列表
        1：获取失败"""
    song_list_url = __get_url(api_parameter_data.common_host,api_parameter_data.song_list_method,
                       type = '1',offset = '0' ,size = '100' , fields = 'song_id%2Ctitle%2Cauthor%2Calbum_title%2Cpic_big%2Cpic_small%2Chavehigh%2Call_rate%2Ccharge%2Chas_mv_mobile%2Clearn%2Csong_source%2Ckorean_bb_song')    #获取榜单页面的具体信息

    song_list = __get_first_three_song_name_from_songlist(number,song_list_url)      #根据榜单的url获取其中的前三首歌
    if song_list == 1:
        return 1
    return song_list

def get_play_list_collector_user_id_list():
    """获取收藏歌单的用户id的列表
    返回值：
        在获取信息失败的时候会返回1"""
    list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_method,
                         channename = urllib.parse.quote('全部'),order_type = '1',offset='0',size='100')

    list_id = __get_first_list_id_from_playlist(1,list_url)         #获取list_id
    if list_id == 1:
        return 1
    play_list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_page_method,
                    list_id = list_id,offset = '0',withsong = '1',withcount = '1',size = '100')           #根据list_id获取具体歌单页面的url，从这里能得到歌单的信息

    user_id_list = __get_collector_user_id_list(play_list_url)
    return user_id_list

def get_first_play_list_name():
    """获取当前最热歌单第一名的歌单的歌单名
    步骤：
        1.获取最热歌单列表的url
        2.根据url，获取第一个歌单的list_id
    返回值：
        song_list：歌曲名列表
        1:获取失败"""
    list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_method,
                    channelname = urllib.parse.quote('全部'),order_type = '1',offset='0',size='100')

    list_name = __get_first_list_id_from_playlist(2,list_url)         #获取title
    if list_name == 1:
        return 1
    return list_name

def get_first_play_list_first_song_name(number):
    """获取当前最热歌单第一名的歌单的前number首歌曲名
    步骤：
        1.获取最热歌单列表的url
        2.根据url，获取第一个歌单的list_id
        3.根据list_id，拼接出对应歌单的url
        4.根据url，获取歌单中的歌曲信息
    返回值：
        song_list：歌曲名列表
        1:获取失败"""
    list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_method,
                    channelname = urllib.parse.quote('全部'),order_type = '1',offset='0',size='100')

    list_id = __get_first_list_id_from_playlist(1,list_url)         #获取list_id
    if list_id == 1:
        return 1

    play_list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_page_method,
                    list_id = list_id,offset = '0',withsong = '1',withcount = '1',size = '100')           #根据list_id获取具体歌单页面的url，从这里能得到歌单的信息

    song_list = __get_first_three_song_name_from_playlist(number,play_list_url)       #根据具体的歌单id，获取歌单中的前三首歌名
    if song_list == 1:
        return 1
    return song_list

def get_first_play_list_first_song_have_mv():
    """判断当前最热歌单第一名的歌单的第一首歌是否有mv
    步骤：
        1.获取最热歌单列表的url
        2.根据url，获取第一个歌单的list_id
        3.根据list_id，拼接出对应歌单的url
        4.根据url，获取歌单中的歌曲信息，根据这些信息判断第一首歌是否有mv
    返回值：
        1:获取失败"""
    list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_method,
                    channelname = urllib.parse.quote('全部'),order_type = '1',offset='0',size='100')

    list_id = __get_first_list_id_from_playlist(1,list_url)         #获取list_id
    if list_id == 1:
        return 1

    play_list_url = __get_url(api_parameter_data.common_host,api_parameter_data.play_list_page_method,
                    list_id = list_id,offset = '0',withsong = '1',withcount = '1',size = '100')           #根据list_id获取具体歌单页面的url，从这里能得到歌单的信息

    first_song_have_mv_code = __get_first_song_have_mv_code(play_list_url)           #跟据url获取第一首歌曲是否有mv的code
    if first_song_have_mv_code == 1:
        return 1

    return first_song_have_mv_code

def get_user_collect_song_list():
    """根据token获取对应用户的收藏信息
    返回值：
        1：获取失败"""
    token = __get_cookie()
    if token == 1:
        return 1
    url = __get_url(api_parameter_data.common_host,api_parameter_data.get_collect_method,
                    pn = '0',rn = '50',token_ = token)
    dic = __get_info(url)
    if dic == 1:
        return 1
    song_name_list = {}
    i = 0
    total = dic['total']
    while i < total:
        song_name_list[i] = dic['result'][i]['title']
        i += 1

    return song_name_list
