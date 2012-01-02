import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.SourceDataLine;

public class Bytebeat {
    public static final int BUF_SIZE = 32000;
    public static final int SAMPLE_RATE = 8000;
    
    public static void main(String[] args) throws Exception { 
        AudioFormat aFormat = new AudioFormat(SAMPLE_RATE, 8, 1, true, false);
        SourceDataLine line = AudioSystem.getSourceDataLine(aFormat);
        line.open(aFormat, BUF_SIZE);
        line.start();
        long t = 0;
        byte[] buf = new byte[BUF_SIZE];
        while(true) {
            for(int i = 0; i < BUF_SIZE; i++, t++) buf[i] = getSample(t);
            line.write(buf, 0, buf.length);
        }
    }
    
    public static byte getSample(long t) {
        // akx 2011-10-05 http://twitter.com/#!/akx
        return (byte) ((((((t*((t>>9|t>>13)&15))&255/15)*9)%(1<<7))<<2)%6<<4);
    }
}
