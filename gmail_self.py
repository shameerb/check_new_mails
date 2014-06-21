import urllib2
import untangle

FEED_URL="https://mail.google.com/mail/feed/atom"

def get_mails(user,paswd):
    auth_handler=urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm="New mail feed",
        uri="https://mail.google.com",
        user="{user}@gmail.com".format(user=user),
        passwd=paswd
        
    )
    opener=urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed=urllib2.urlopen(FEED_URL)
    return feed.read()


if __name__=="__main__":
    import getpass

    user = raw_input("Username : ")
    paswd = getpass.getpass("Password : ")
    xml=get_mails(user,paswd)
    

    o=untangle.parse(xml)
    print o.feed.title.cdata
    print '*'*40
    for i in o.feed.entry:
        print "SUBJECT : \t",i.title.cdata
        print "CONTENT : \t",i.summary.cdata
        print '*'*40
    

