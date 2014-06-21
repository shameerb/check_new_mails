import urllib2
import untangle
from Tkinter import *

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
	cnt=int(o.feed.fullcount.cdata)
	
	root=Tk()
	text_out=[]
	for i in range(cnt):
		text_out.append(Text(root))
	#text_out = Text(root)
	for ind,i in enumerate(o.feed.entry):
		text_out[ind].insert(INSERT, "MAIL NO : \t"+str(ind+1))
		text_out[ind].insert(INSERT, "\nSUBJECT : \t"+i.title.cdata)
		text_out[ind].insert(END, "\nCONTENT : \n\t"+i.summary.cdata)
		text_out[ind].pack()
	root.mainloop()
	
	    

