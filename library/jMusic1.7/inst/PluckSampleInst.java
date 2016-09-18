import jm.audio.io.*;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;

public final class PluckSampleInst extends jm.audio.Instrument{
	private String fileName;
	
	public PluckSampleInst() {
                this("Hello.au");
        }
        
        public PluckSampleInst(String str) {
                this.fileName = str;
        }
        	
	/** Initialisation method used to build the objects that this instrument
         *  will use 
         */
	public void createChain(){
		SampleIn si = new SampleIn(this, fileName);
                Pluck plk = new Pluck(si);
		Volume vol = new Volume(plk);
		StereoPan span = new StereoPan(vol);
                Envelope env = new Envelope(span, new double[] {0.0, 0.0, 0.01, 1.0, 0.99, 1.0, 1.0, 0.0});
		SampleOut sout = new SampleOut(env);
	}
}



