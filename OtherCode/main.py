import tweepy, time, sys

print("Start file")

#argfile = str(sys.argv[1])

print("Setting up URL connection")

#Setting Up Authentication to access the Twitter API
c_k = 'XqiqSs625kgEdD4Igrix2Or0l'
c_s = 'UmktY91ehm8xlmiiopfiJUkIhGwaYrbFSVTtGDumrC2d6PmJ56'
auth = tweepy.OAuthHandler(c_k, c_s)

a_k = '1185020038446641152-ZKhguI4t3eNd'
a_s = 'DsitcyisTXkrymnnO0plDRJpo11AeuiWBUadkAVWfDIC9'
auth.set_access_token(a_k, a_s)

api = tweepy.API(auth)
print(api)

#filename = open(argfile, 'r')
#f = filename.readlines()
#filename.close()

#print("post file connection")

api.verify_credentials()

#api.update_status("Hello World")
#for line in f:
#	print("Establishing connection")
#	api.update_status(line)
#	time.sleep(600)#tweeting every 10 minutes

#900 = 15 minutes
#So, 1 minute = 900/15 = 60
#So, 10 minutes = 600 
