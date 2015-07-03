import re
import urllib2

class GetIp:
	def getip(self):
		url = "http://syzj.sinaapp.com/whatIsMyIp.php"
		response = urllib2.urlopen(url)
		html = response.read()
		ip = re.search('\d+\.\d+\.\d+\.\d+',html).group(0)
		return ip

if __name__ == '__main__':
	getIp = GetIp()
	ip = getIp.getip()
	print(ip)
