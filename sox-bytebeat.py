# -- encoding: utf-8 --

import struct, subprocess, optparse, array

def play(stream, t_func):
	BUF_SIZE = 4096
	buffer = array.array("B", [0] * BUF_SIZE)

	t = 0
	while 1:
		for i in xrange(BUF_SIZE):
			buffer[i] = t_func(t) % 256
			t += 1
		stream.write(buffer.tostring())

def open_sox(sample_rate):
	return subprocess.Popen("sox -r %d -u -1 -c 1 -t raw - -d" % (int(sample_rate)), stdin = subprocess.PIPE)

def cmd_main():
	op = optparse.OptionParser()
	op.add_option("-s", "--sample-rate", default = 8000, type = int)
	opt, args = op.parse_args()
	if not args:
		op.error("Missing formula")
	func = eval("lambda t: (%s)" % args[0]) # eval is obviously usually a bad idea. not here.
	
	sox = open_sox(opt.sample_rate)
	try:
		play(sox.stdin, func)
	finally:
		sox.stdin.close()
		sox.terminate()
		
if __name__ == '__main__':
	cmd_main()