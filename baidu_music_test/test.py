# --*-- coding=utf-8 --*--

from urllib.request import urlopen
import json
import time
import urllib.parse
from urllib.parse import quote
from baidu_music_test.data import api_parameter_data

def get_url(host='',method='',**kwargs):
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

def get_first_list_id_from_playlist(url = ''):
    """功能：
            获取对应歌单列表的第一个歌单list_id"""
    page = urlopen(url)
    data = page.read()
    dic = json.loads(data)

    list_id = dic['diyInfo'][0]['list_id']
    #print('获取的list_id为：'+list_id)
    return list_id

def get_first_three_song_name_from_songlist(number,url = ''):
    """功能：
            获取新歌榜前number首歌曲名
        参数:
            url:
            number：获取的歌曲名数量"""
    page=urlopen(url)
    data=page.read()
    dic = json.loads(data)

    print('该榜单的前',number,'首歌曲名为：')
    song_name_list={}
    i=0
    while i < number:
        song_name_list[i] = dic['song_list'][i]['title']
        print(i+1,':',song_name_list[i])
        i += 1
    return song_name_list

def get_first_three_song_name_from_playlist(number,url = ''):
    """功能：
            获取对应url歌单的前number首歌曲名
        参数：
            number：获取的歌曲名数量"""

    page=urlopen(url)
    data=page.read()
    dic = json.loads(data)

    song_list_name = dic['result']['info']['list_title']
    print('该歌单名为：',song_list_name)
    song_name_list={}
    print('该歌单的前',number,'首歌名为：')
    i=0
    while i < number:
        song_name_list[i] = dic['result']['songlist'][i]['title']
        print(i+1,':',song_name_list[i])
        i += 1
    return song_name_list




def get_first_play_list_first_song_name(number):
    """获取当前最热歌单第一名的歌单的前number首歌曲名
    步骤：
        1.获取最热歌单列表的url
        2.根据url，获取第一个歌单的list_id
        3.根据list_id，拼接出对应歌单的url
        4.根据url，获取歌单中的歌曲信息"""
    list_url = get_url(api_parameter_data.list_page_host,api_parameter_data.play_list_method,
                    channelname = urllib.parse.quote('全部'),order_type = '1',offset='0',size='100')

    list_id = get_first_list_id_from_playlist(list_url)         #获取list_id

    play_list_url = get_url(api_parameter_data.list_page_host,api_parameter_data.play_list_page_method,
                    list_id = list_id,offset = '0',withsong = '1',withcount = '1',size = '100')           #根据list_id获取具体歌单页面的url，从这里能得到歌单的信息

    song_list = get_first_three_song_name_from_playlist(number,play_list_url)       #根据具体的歌单id，获取歌单中的前三首歌名
    return song_list


def get_new_song_list_first_song_name(number):
    """获取新歌榜的前number首歌曲的歌曲名"""
    song_list_url = get_url(api_parameter_data.list_page_host,api_parameter_data.song_list_method,
                       type = '1',offset = '0' ,size = '100' , fields = 'song_id%2Ctitle%2Cauthor%2Calbum_title%2Cpic_big%2Cpic_small%2Chavehigh%2Call_rate%2Ccharge%2Chas_mv_mobile%2Clearn%2Csong_source%2Ckorean_bb_song')    #获取榜单页面的具体信息

    song_list = get_first_three_song_name_from_songlist(number,song_list_url)      #根据榜单的url获取其中的前三首歌
    return song_list






list = get_first_play_list_first_song_name(3)
get_new_song_list_first_song_name(3)

print(list)