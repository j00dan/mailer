import subprocess
import sys
import urlparse

url = str(sys.argv[1])
r = urlparse.urlsplit(url)
final_url = urlparse.urlunsplit((r.scheme, r.netloc, r.path, '', ''))

cmd = 'echo "{}" | mail -s "Phishing URL" <Email Address>'.format(final_url)

#print cmd

subprocess.Popen(cmd, shell=True)
