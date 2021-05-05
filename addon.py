from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/recodedecode"
url2 = "https://feeds.megaphone.fm/vergecast"
url3 = "https://feeds.megaphone.fm/wyptb"
url4 = "https://feeds.megaphone.fm/verge-extras"
url5 = "https://feeds.megaphone.fm/converge"
url6 = "https://feeds.megaphone.fm/ctrl-walt-delete"
url7 = "https://feeds.megaphone.fm/whats-tech"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.megaphone.fm/wKfCc1QFQ0vLPxussqa1NkvPj2YDRu88j2n3ExlCfnE/plain/s3://megaphone-prod/podcasts/5c6a4f4a-e69c-11e8-8066-17a10182e4c8/image/uploads_2F1603744706793-t0bv7cr1mjk-3bf6145e5104a8bb7e466f07c559b548_2FDecoder_TileArt.png"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/e4c412e6-e1f0-11e8-9bde-83f9d376f059/image/uploads_2F1567105071975-o6k62rq8bin-247a9596590486c06b16976bed1cefbc_2FVergecast_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/1c380136-c5ea-11ea-a5f2-f7569ee7bbca/image/uploads_2F1594741984266-8r1cwe1antd-1c79bcdcebb09d7f1726a4ada9d709c6_2FWYPTB_Cover_Art_071320.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/48d31926-0a3b-11ea-9a69-df810554280a/image/uploads_2F1574708739653-9s2tjxmh4p-23816ebb797a95653b0c65d46e6acf1b_2FPirate_Radio_Covers_RGB_Podcast_002.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/d1561546-e183-11e8-b655-3f66eb01c2a5/image/007c2fbcb44c32020cf2bde1678ed4ee878f80a33439929954194d7336a12d616f7d1b0ae8fd9779035657c291c83083116680b5983c1f90a6a7e60bfb1213c7.jpeg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/b7b493fe-e3a1-11e8-94f7-7b11ec11f879/image/e828867aad821a60cdad95ebfd64163e0fc1b85451081c9c15115e3b910aeb39b1de1db8ed54d1953598236f1b34efea57f6ca4fb2be3bd8b2106ad7215e35f7.jpeg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/a2328c02-e185-11e8-ba80-47d7c905440e/image/55bdd62697086f45a1984f41d0a22139471b05fd1712978e049a6dec35164fb63347e8a067410c519f3f03eceb3140a7923627ec382f48a46c8b9587a65c2c1a.jpeg?ixlib=rails-2.1.2&w=400&h=400"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

if __name__ == '__main__':
    plugin.run()
