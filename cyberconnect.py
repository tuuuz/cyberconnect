import json
from collections import OrderedDict

fw = open('follow.html', 'w')

if __name__ == '__main__':
    with open("data.json", "r") as f:
        json_str = f.read()
        rsp = json.loads(json_str, object_pairs_hook=OrderedDict)
        #print(rsp['data']['identity']['followerCount'])
        followerCount = rsp['data']['identity']['followerCount']
        followingCount = rsp['data']['identity']['followingCount']
        if followerCount > followingCount:
            #print(rsp['data']['identity']['followers']['list'][:followerCount - followingCount])
            for i in rsp['data']['identity']['followers']['list'][:followerCount - followingCount]:
                #print(i['address'])
                if len(i['domain']) > 0:
                    url = 'https://app.cyberconnect.me/address/%s'%i['domain']
                else:
                    url = 'https://app.cyberconnect.me/address/%s'%i['address']
                print(url)
                print('<a href="%s" target="_blank">%s</a><br/>'%(url, url), file=fw)
                    

fw.close()
